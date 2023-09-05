# Generated by Django 4.2 on 2023-07-11 04:49

import account.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_useraccount_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=account.models.CustomDateTimeField(default=datetime.datetime(2023, 7, 11, 4, 49, 55, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]