# Generated by Django 4.1.13 on 2025-01-02 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='featured',
            new_name='is_live',
        ),
    ]
