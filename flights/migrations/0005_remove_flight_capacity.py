# Generated by Django 3.1.2 on 2020-11-30 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20201130_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='capacity',
        ),
    ]