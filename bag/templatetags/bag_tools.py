from django import template
import decimal


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    price = price.strip()
    if price:
        return decimal.Decimal(price) * quantity