# Generated by Django 4.0.3 on 2022-04-04 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atrybut',
            fields=[
                ('id_atrybut', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '03 Atrybut',
            },
        ),
        migrations.CreateModel(
            name='Dana',
            fields=[
                ('id_dana', models.AutoField(primary_key=True, serialize=False)),
                ('wartosc', models.FloatField()),
                ('id_atrybut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict.atrybut')),
            ],
            options={
                'verbose_name_plural': '05 Dana',
            },
        ),
        migrations.CreateModel(
            name='IrisImportExport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sepal_length', models.FloatField()),
                ('sepal_width', models.FloatField()),
                ('petal_length', models.FloatField()),
                ('petal_width', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Iris Imported from CSV ',
            },
        ),
        migrations.CreateModel(
            name='Klasa',
            fields=[
                ('id_klasa', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '02 Klasa',
            },
        ),
        migrations.CreateModel(
            name='Obserwacja',
            fields=[
                ('id_obserwacja', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '04 Obserwacja',
            },
        ),
        migrations.CreateModel(
            name='PredictionResults',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sepal_length', models.FloatField()),
                ('sepal_width', models.FloatField()),
                ('petal_length', models.FloatField()),
                ('petal_width', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Iris User Input History ',
            },
        ),
        migrations.CreateModel(
            name='Zbior',
            fields=[
                ('id_zbior', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '01 Zbior',
            },
        ),
        migrations.DeleteModel(
            name='PredResults',
        ),
        migrations.AddField(
            model_name='klasa',
            name='id_zbior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='predict.zbior'),
        ),
        migrations.AddField(
            model_name='dana',
            name='id_obserwacja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict.obserwacja'),
        ),
        migrations.AddField(
            model_name='atrybut',
            name='id_zbior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict.zbior'),
        ),
    ]
