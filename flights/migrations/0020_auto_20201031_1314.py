# Generated by Django 3.1.2 on 2020-10-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0019_auto_20201021_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='ph_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]