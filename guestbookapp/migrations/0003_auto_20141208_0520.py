# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbookapp', '0002_auto_20141208_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guests',
            name='device',
            field=models.CharField(max_length=50, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guests',
            name='entry_date',
            field=models.TimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guests',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guests',
            name='ip_address',
            field=models.IPAddressField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guests',
            name='o_s',
            field=models.CharField(max_length=50, null=True, editable=False),
            preserve_default=True,
        ),
    ]
