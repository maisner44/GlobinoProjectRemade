# Generated by Django 4.2 on 2023-05-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departments',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.RemoveField(
            model_name='departments',
            name='default_value',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='max',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='min',
        ),
        migrations.AddField(
            model_name='departments',
            name='default_value_a',
            field=models.IntegerField(default=1, verbose_name='default_value_air'),
        ),
        migrations.AddField(
            model_name='departments',
            name='default_value_h',
            field=models.IntegerField(default=1, verbose_name='default_value_humidity'),
        ),
        migrations.AddField(
            model_name='departments',
            name='default_value_t',
            field=models.IntegerField(default=1, verbose_name='default_value_temperature'),
        ),
        migrations.AddField(
            model_name='departments',
            name='max_a',
            field=models.IntegerField(default=1, verbose_name='max_value_air'),
        ),
        migrations.AddField(
            model_name='departments',
            name='max_h',
            field=models.IntegerField(default=1, verbose_name='max_value_humidity'),
        ),
        migrations.AddField(
            model_name='departments',
            name='max_t',
            field=models.IntegerField(default=1, verbose_name='max_value_temperature'),
        ),
        migrations.AddField(
            model_name='departments',
            name='min_a',
            field=models.IntegerField(default=0, verbose_name='min_value_air'),
        ),
        migrations.AddField(
            model_name='departments',
            name='min_h',
            field=models.IntegerField(default=0, verbose_name='min_value_humidity'),
        ),
        migrations.AddField(
            model_name='departments',
            name='min_t',
            field=models.IntegerField(default=0, verbose_name='min_value_temperature'),
        ),
    ]