# Generated by Django 3.2.9 on 2021-12-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meditation',
            name='minutes',
            field=models.IntegerField(default=10, max_length=60),
            preserve_default=False,
        ),
    ]
