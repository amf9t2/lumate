# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guests',
            fields=[
                ('GuestID', models.AutoField(serialize=False, primary_key=True)),
                ('LastName', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('IPAddress', models.IPAddressField(editable=False)),
                ('EntryDate', models.TimeField(auto_now=True)),
                ('OS', models.CharField(max_length=50, editable=False)),
                ('Device', models.CharField(max_length=50, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
