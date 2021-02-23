from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

import json
import time


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL
            }
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        print("Step 1")
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        print("Step 2")
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        print("Shipping Details: {}".format(shipping_details))
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        print("Step 3")
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        print("Step 4")
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                default_phone_number = shipping_details.phone,
                default_country = shipping_details.address.country,
                default_postcode = shipping_details.address.postal_code,
                default_town_or_city = shipping_details.address.city,
                default_street_address1 = shipping_details.address.line1,
                default_street_address2 = shipping_details.address.line2,
                default_county = shipping_details.address.state,
                profile.save()

        print("Step 5")
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                print("Name:               {}".format(shipping_details.name))
                print("Email:              {}".format(billing_details.email))
                print("Phone:              {}".format(shipping_details.phone))
                print("Country:            {}".format(shipping_details.address.country))
                print("PostCode:           {}".format(shipping_details.address.postal_code))
                print("Town:               {}".format(shipping_details.address.city))
                print("Street1:            {}".format(shipping_details.address.line1))
                print("Street2:            {}".format(shipping_details.address.line2))
                print("County:             {}".format(shipping_details.address.state))
                print("Grand:              {}".format(shipping_details.grand_total))
                print("Bag:                {}".format(shipping_details.bag))
                print("StripePID:          {}".format(shipping_details.pid))
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                print("We are in order does not exists - attempt: {}".format(attempt))
                attempt += 1
                time.sleep(1)
                
        print("Step 6")
        if order_exists:
            self._send_confirmation_email(order)
            print("Order in StripeWH class: {}".format(order))
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCEESS: verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        print("Step 7")
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCEESS: Created order in webhook',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
