# Generated by Django 2.1.1 on 2018-11-06 17:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brokenChains', '0002_auto_20181106_1723'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='habit',
            unique_together={('owner', 'name')},
        ),
    ]