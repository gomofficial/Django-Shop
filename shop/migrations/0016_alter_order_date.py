# Generated by Django 3.2.6 on 2021-09-05 05:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 5, 5, 53, 50, 352207, tzinfo=utc), verbose_name='تاریخ ثبت'),
        ),
    ]