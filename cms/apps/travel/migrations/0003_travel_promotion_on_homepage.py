# Generated by Django 2.1.2 on 2018-12-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20181222_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='promotion_on_homepage',
            field=models.BooleanField(default=False),
        ),
    ]