# Generated by Django 2.2.1 on 2020-02-08 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_bloky',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=30)),
                ('odkaz', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Priklady_do_testu_k_maturite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zadani', models.TextField()),
                ('reseni', models.TextField()),
                ('priklad_v_testu', models.IntegerField()),
                ('A', models.CharField(max_length=300)),
                ('B', models.CharField(max_length=300)),
                ('C', models.CharField(max_length=300)),
                ('D', models.CharField(max_length=300)),
                ('E', models.CharField(max_length=300)),
                ('Spravna_odpoved', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skola', models.CharField(choices=[('1', 'ZŠ'), ('2', 'SŠ')], default='ZŠ', max_length=2)),
                ('tema', models.CharField(max_length=30)),
                ('podtema', models.CharField(blank=True, max_length=50)),
                ('kapitola', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Téma',
                'verbose_name_plural': 'Témata',
            },
        ),
        migrations.CreateModel(
            name='Pocetni_priklady',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zadani', models.TextField()),
                ('reseni', models.TextField()),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matematikuj.Tema')),
            ],
            options={
                'verbose_name': 'Příklad na SŠ',
                'verbose_name_plural': 'Příklady pro SŠ',
            },
        ),
    ]
