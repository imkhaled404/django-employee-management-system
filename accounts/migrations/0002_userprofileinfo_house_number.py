# Generated by Django 2.2 on 2019-04-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='house_number',
            field=models.CharField(default=1, max_length=20, verbose_name='Numer domu'),
            preserve_default=False,
        ),
    ]
