from django import template
from decimal import Decimal


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_saleprice')
def calc_saleprice(price, discount_percent):
    sale_price = price - Decimal(price * (discount_percent/100))
    return round(sale_price, 2)
