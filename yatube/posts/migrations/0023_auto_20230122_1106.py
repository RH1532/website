# Generated by Django 2.2.16 on 2023-01-22 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20230122_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подписку', 'verbose_name_plural': 'Подписки'},
        ),
    ]
