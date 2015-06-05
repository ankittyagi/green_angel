from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True)
    verb = models.CharField(max_length=255)

    target_content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj')
    target_object_id = models.PositiveIntegerField(null=True, db_index=True)
    target = GenericForeignKey('target_content_type','target_object_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
