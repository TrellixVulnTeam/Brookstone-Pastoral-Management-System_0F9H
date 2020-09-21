# Generated by Django 2.2.6 on 2020-09-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManager', '0007_auto_20200822_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='DenyEntryCheckIn',
            field=models.CharField(choices=[('Deny Entry?', 'Deny Entry?'), ('No', 'No'), ('Yes', 'Yes')], default='Deny Entry?', max_length=3, verbose_name='Deny Entry'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='MetRequirements',
            field=models.CharField(choices=[('Met Requirements?', 'Met Requirements?'), ('No', 'No'), ('Yes', 'Yes')], default='Met Requirements?', max_length=3, verbose_name='Met Requirements?'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='PC',
            field=models.CharField(choices=[('Choose Pastoral Centre', 'Choose Pastoral Centre'), ('Pastoral Center 1', 'Pastoral Center 1'), ('Pastoral Center 2', 'Pastoral Center 2'), ('Pastoral Center 3', 'Pastoral Center 3'), ('Pastoral Center 4', 'Pastoral Center 4'), ('Pastoral Center 5', 'Pastoral Center 5'), ('Pastoral Center 6', 'Pastoral Center 6')], default='Choose Pastoral Centre', max_length=20, verbose_name='Pastoral Center'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='ReasonCheckInPC',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='ReasonPass',
            field=models.CharField(default='', max_length=200, verbose_name='Reason'),
        ),
    ]
