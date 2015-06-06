# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0007_auto_20150606_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantation',
            name='campaign',
        ),
        migrations.AddField(
            model_name='plantation',
            name='zone',
            field=models.ForeignKey(default=1, to='app_users.CampaignZone'),
            preserve_default=False,
        ),
    ]
