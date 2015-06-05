__author__ = 'Tarun Behal'

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


User.profile = property(
    lambda u: UserProfile.objects.get_or_create(user=u)[0])
