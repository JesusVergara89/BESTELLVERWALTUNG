# Generated by Django 5.0.6 on 2024-07-17 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_line',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orders_line',
            old_name='product_id',
            new_name='product',
        ),
    ]
