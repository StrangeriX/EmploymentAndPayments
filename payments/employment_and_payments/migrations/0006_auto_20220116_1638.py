# Generated by Django 3.1 on 2022-01-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment_and_payments', '0005_auto_20220116_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ocenapracownika',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'Ratrings'},
        ),
        migrations.AlterModelOptions(
            name='swiadectwopracy',
            options={'verbose_name': 'Work certificates', 'verbose_name_plural': 'Work certificates'},
        ),
    ]
