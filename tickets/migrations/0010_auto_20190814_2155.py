# Generated by Django 2.2 on 2019-08-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20190814_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Immediate'), (2, 'Semi-Immediate'), (3, 'Not-Immediate')], default='NIM', max_length=20),
        ),
    ]
