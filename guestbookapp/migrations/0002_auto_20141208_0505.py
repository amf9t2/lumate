# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbookapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guests',
            old_name='Device',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='guests',
            old_name='EntryDate',
            new_name='entry_date',
        ),
        migrations.RenameField(
            model_name='guests',
            old_name='FirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='guests',
            old_name='GuestID',
            new_name='guest_id',
        ),
        migrations.RenameField(
            model_name='guests',
            old_name='IPAddress',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='guests',
            old_name='LastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='guests',
            old_name='OS',
            new_name='o_s',
        ),
    ]
