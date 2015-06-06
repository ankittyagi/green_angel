# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app_users.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_userprofile_zones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantation',
            name='photo',
            field=models.ImageField(upload_to=app_users.models.upload_path),
        ),
    ]
