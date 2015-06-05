# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_auto_20150605_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantation',
            name='name',
        ),
    ]
