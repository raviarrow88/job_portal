# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequests',
            name='request_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='jobrequests',
            name='request_on',
        ),
        migrations.AddField(
            model_name='jobrequests',
            name='request_on',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]
