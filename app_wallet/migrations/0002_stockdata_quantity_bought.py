# Generated by Django 5.0.6 on 2024-05-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='quantity_bought',
            field=models.IntegerField(default=0),
        ),
    ]
