# Generated by Django 2.2.6 on 2020-08-22 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManager', '0006_checkin_denentrycheckin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='DenEntryCheckIn',
            new_name='DenyEntryCheckIn',
        ),
    ]
