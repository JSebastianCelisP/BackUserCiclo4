# Generated by Django 3.2.8 on 2021-11-25 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreriauserapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='saldo',
        ),
    ]
