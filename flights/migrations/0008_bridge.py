# Generated by Django 3.1.2 on 2020-12-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_auto_20201214_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengers', models.ManyToManyField(blank=True, related_name='relatives', to='flights.Passenger')),
            ],
        ),
    ]
