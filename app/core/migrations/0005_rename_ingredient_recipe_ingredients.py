# Generated by Django 3.2.23 on 2023-11-23 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231123_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]