# Generated by Django 2.1.2 on 2019-01-08 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20190108_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='mourning_mode',
            field=models.BooleanField(default=False),
        ),
    ]