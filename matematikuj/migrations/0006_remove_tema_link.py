# Generated by Django 2.2.1 on 2020-02-08 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matematikuj', '0005_auto_20200208_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tema',
            name='link',
        ),
    ]