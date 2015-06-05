# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import app_users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_users', '0002_campaign_campaignzone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('photo', models.FileField(default=False, upload_to=app_users.models.upload_path, blank=True)),
                ('points', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'approve', b'Approved'), (b'reject', b'Rejected')])),
                ('campaign', models.ForeignKey(to='app_users.Campaign')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='campaignzone',
            name='total_plants',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='campaignzone',
            name='total_points',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
