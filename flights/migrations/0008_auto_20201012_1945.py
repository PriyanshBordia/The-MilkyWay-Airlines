# Generated by Django 3.0.6 on 2020-10-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_auto_20201012_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='ph_no',
            field=models.IntegerField(),
        ),
    ]
