# Generated by Django 2.2 on 2019-08-14 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20190814_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['priority']},
        ),
    ]
