# Generated by Django 2.2.6 on 2022-12-29 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20221229_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name_plural': 'Посты'},
        ),
    ]
