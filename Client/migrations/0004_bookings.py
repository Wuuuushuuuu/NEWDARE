# Generated by Django 3.2 on 2021-05-24 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Contact_no', models.CharField(max_length=20)),
                ('Date', models.DateField()),
                ('Concern', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=60)),
            ],
        ),
    ]
