# Generated by Django 2.2.1 on 2020-02-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matematikuj', '0004_tema_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='link',
            field=models.CharField(blank=True, default='pro ZS 6. ročník -> 6rocnik', max_length=50),
        ),
    ]
