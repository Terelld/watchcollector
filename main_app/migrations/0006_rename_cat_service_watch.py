# Generated by Django 4.2.4 on 2023-08-09 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='cat',
            new_name='watch',
        ),
    ]
