# Generated by Django 3.1.6 on 2021-05-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210521_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_link',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]