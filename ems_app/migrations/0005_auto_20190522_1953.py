# Generated by Django 2.2 on 2019-05-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0004_auto_20190522_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidaymodel',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='Data czy_zatwierdzone'),
        ),
        migrations.AlterField(
            model_name='holidaymodel',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='Czy zakończone'),
        ),
    ]