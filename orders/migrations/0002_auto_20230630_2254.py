# Generated by Django 3.0.10 on 2023-07-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='type',
            field=models.CharField(default='', max_length=150),
        ),
    ]
