# Generated by Django 2.2.1 on 2020-02-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matematikuj', '0003_auto_20200208_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='link',
            field=models.CharField(default=models.CharField(max_length=30), max_length=50),
        ),
    ]
