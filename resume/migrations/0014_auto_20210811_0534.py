# Generated by Django 3.1.6 on 2021-08-11 05:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0013_auto_20210622_0217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='User_Email',
        ),
    ]