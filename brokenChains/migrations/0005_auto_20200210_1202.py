# Generated by Django 2.2.10 on 2020-02-10 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokenChains', '0004_auto_20181217_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='stop_date',
            field=models.DateField(default=datetime.date(2020, 3, 2)),
        ),
    ]
