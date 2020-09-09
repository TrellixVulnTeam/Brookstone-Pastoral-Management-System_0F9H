# Generated by Django 2.2.6 on 2020-08-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManager', '0004_auto_20200817_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='AccompanyGuardian',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Accompanying Guardian'),
        ),
        migrations.AddField(
            model_name='checkin',
            name='AccompanyGuardianPhone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Guardian Phone'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='PC',
            field=models.CharField(choices=[('----', '----'), ('Pastoral Center 1', 'Pastoral Center 1'), ('Pastoral Center 2', 'Pastoral Center 2'), ('Pastoral Center 3', 'Pastoral Center 3'), ('Pastoral Center 4', 'Pastoral Center 4'), ('Pastoral Center 5', 'Pastoral Center 5'), ('Pastoral Center 6', 'Pastoral Center 6')], default='----', max_length=20, verbose_name='Pastoral Center'),
        ),
    ]