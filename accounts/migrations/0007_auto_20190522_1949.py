# Generated by Django 2.2 on 2019-05-22 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190522_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_manager',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_manager', to=settings.AUTH_USER_MODEL, verbose_name='Kierownik'),
        ),
    ]