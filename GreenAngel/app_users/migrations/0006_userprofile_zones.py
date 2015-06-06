# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_auto_20150606_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zones',
            field=models.ManyToManyField(related_name=b'zones', to='app_users.CampaignZone', blank=True),
            preserve_default=True,
        ),
    ]
