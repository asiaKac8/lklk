# Generated by Django 4.0.3 on 2022-04-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_atrybut_dana_irisimportexport_klasa_obserwacja_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversalTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('a2', models.FloatField()),
                ('a3', models.FloatField()),
                ('a4', models.FloatField()),
                ('a5', models.FloatField()),
                ('a6', models.FloatField()),
                ('a7', models.FloatField()),
                ('a8', models.FloatField()),
                ('a9', models.FloatField()),
                ('a10', models.FloatField()),
                ('c1', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'UniversalTable',
            },
        ),
    ]