# Generated by Django 4.2 on 2023-07-01 12:33

import account.models
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_useraccount_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=account.models.CustomDateTimeField(default=datetime.datetime(2023, 7, 1, 12, 33, 37, tzinfo=datetime.timezone.utc)),
        ),
    ]
