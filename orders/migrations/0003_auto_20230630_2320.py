# Generated by Django 3.0.10 on 2023-07-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20230630_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='name_delivery',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]