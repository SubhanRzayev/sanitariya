from core.models import Information
from django.template import Library
from core.models import *
from product.models import *
from services.models import *


register = Library()

@register.simple_tag
def footer_products():
    return Product.objects.order_by('title')[:7]


@register.simple_tag
def servic():
    return Services.objects.order_by('title')[:7]


# @register.simple_tag
# def header_service():
#     return Services.objects.order_by('title')[:7]


@register.simple_tag
def footer_information():
    return Information.objects.all()



