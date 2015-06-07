from django import template
from django.utils import timezone
from app_users.models import *

register = template.Library()


@register.assignment_tag(takes_context=True)
def myplantationtotal(context, campaign, user):
    return Plantation.objects.filter(zone__campaign=campaign, user=user).count()


@register.assignment_tag(takes_context=True)
def myplantationtozone(context, zone, user):
    return Plantation.objects.filter(zone=zone, user=user)
