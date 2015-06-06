from django import template
from django.utils import timezone
from app_users.models import *

register = template.Library()


@register.assignment_tag(takes_context=True)
def i_quoted(context, meep):
    return meep.quotes.filter(seller=context['seller_user']).count()
