# Generated by Django 2.2.16 on 2023-01-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20230120_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
