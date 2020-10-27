# Generated by Django 3.1.2 on 2020-10-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0014_auto_20201017_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=1000),
        ),
    ]