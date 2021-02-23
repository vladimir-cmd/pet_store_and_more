from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import json


@require_POST
@csrf_exempt
def webhook(request):
    # wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    # try:
    #     sig_header = request.META['HTTP_STRIPE_SINGATURE']
    #     print("sig header in webhook: {}".format(sig_header))
    # except Exception as e:
    #     print("Can't get Stripe Signature: {}".format(str(e)))
    #     print("This is Sig Header: {}".format(sig_header))

    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
        # print("Event in Webhook: {}".format(event))
    except ValueError:
        print("Regular Error")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        print("Stripe Signature Error")
        return HttpResponse(status=400)
    except Exception as e:
        print("Or what the hell in e is:{}".format(str(e)))
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)
    # print("handler in Webhook: {}".format(handler))

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    event_type = event['type']
    # print("Event Type in Webhook: {}".format(event_type))

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    print("Response in Webhook: {}".format(response))
    return response
