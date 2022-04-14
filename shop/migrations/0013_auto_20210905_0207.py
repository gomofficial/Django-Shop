# Generated by Django 3.2.6 on 2021-09-04 21:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210905_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='price',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 21, 37, 8, 438166, tzinfo=utc), verbose_name='تاریخ ثبت'),
        ),
    ]
