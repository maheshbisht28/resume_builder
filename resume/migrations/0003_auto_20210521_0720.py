# Generated by Django 3.1.6 on 2021-05-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_personal_details_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='dob',
            field=models.DateTimeField(),
        ),
    ]
