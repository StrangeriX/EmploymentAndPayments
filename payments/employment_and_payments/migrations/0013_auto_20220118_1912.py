# Generated by Django 3.1 on 2022-01-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment_and_payments', '0012_auto_20220118_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swiadectwopracy',
            name='ocena_pracownika',
        ),
        migrations.RemoveField(
            model_name='swiadectwopracy',
            name='pracownik',
        ),
    ]
