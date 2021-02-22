from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    print("WH Secret in Webhook: {}".format(wh_secret))
    print("Secret key in webhook: {}".format(stripe.api_key))

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SINGATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
        print("Event in Webhook: {}".format(event))
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)
    print("handler in Webhook: {}".format(handler))

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    event_type = event['type']
    print("Event Type in Webhook: {}".format(event_type))

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    print("Response in Webhook: {}".format(response))
    return response
