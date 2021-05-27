# Generated by Django 3.2 on 2021-05-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0005_logged_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='Status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed')], default='Pending', max_length=30),
        ),
    ]