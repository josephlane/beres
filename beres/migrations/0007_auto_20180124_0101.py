# Generated by Django 2.0 on 2018-01-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beres', '0006_auto_20180112_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.URLField(),
        ),
    ]
