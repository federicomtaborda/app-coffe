# Generated by Django 3.0.10 on 2023-07-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20230630_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_product',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
