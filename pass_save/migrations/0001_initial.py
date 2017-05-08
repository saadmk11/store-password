# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
