# Generated by Django 3.2.6 on 2021-09-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210904_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.CharField(max_length=200, verbose_name='قیمت کل'),
        ),
    ]
