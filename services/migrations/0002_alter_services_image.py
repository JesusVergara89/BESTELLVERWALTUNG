# Generated by Django 5.0.6 on 2024-07-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='services'),
        ),
    ]
