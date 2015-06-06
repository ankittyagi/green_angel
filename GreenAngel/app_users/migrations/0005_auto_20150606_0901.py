# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_remove_plantation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignzone',
            name='campaign',
            field=models.ForeignKey(related_name=b'zones', to='app_users.Campaign'),
        ),
    ]
