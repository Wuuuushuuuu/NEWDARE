# Generated by Django 3.1.7 on 2021-05-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dentist_Acct', '0003_alter_dentist_acct_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist_acct',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
