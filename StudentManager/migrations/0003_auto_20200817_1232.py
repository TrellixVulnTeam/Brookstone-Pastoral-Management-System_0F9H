# Generated by Django 2.2.6 on 2020-08-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManager', '0002_auto_20200817_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='PC',
            field=models.CharField(choices=[('----', '----'), ('Pastoral Center 1', 'Pastoral Center 1'), ('Pastoral Center 2', 'Pastoral Center 2'), ('Pastoral Center 3', 'Pastoral Center 3'), ('Pastoral Center 4', 'Pastoral Center 4'), ('Pastoral Center 5', 'Pastoral Center 5'), ('Pastoral Center 6', 'Pastoral Center 6')], default='Pastoral Center 1', max_length=20, verbose_name='Pastoral Center'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='PassCode',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Pass Code'),
        ),
    ]