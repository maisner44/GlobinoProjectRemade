# Generated by Django 4.2 on 2023-05-08 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_modelsensor_dep2_a_modelsensor_dep2_h_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelSensor1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default=0, verbose_name='temperature')),
                ('humidity', models.FloatField(default=1, verbose_name='humidity ')),
                ('air_currents', models.FloatField(default=1, verbose_name='air_currents')),
            ],
            options={
                'verbose_name': 'Sensor1',
                'verbose_name_plural': 'Sensors1',
            },
        ),
        migrations.DeleteModel(
            name='ModelSensor',
        ),
        migrations.AlterField(
            model_name='departments',
            name='default_value_a',
            field=models.FloatField(default=1, verbose_name='default_value_air'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='default_value_h',
            field=models.FloatField(default=1, verbose_name='default_value_humidity'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='default_value_t',
            field=models.FloatField(default=1, verbose_name='default_value_temperature'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='max_a',
            field=models.FloatField(default=1, verbose_name='max_value_air'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='max_h',
            field=models.FloatField(default=1, verbose_name='max_value_humidity'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='max_t',
            field=models.FloatField(default=1, verbose_name='max_value_temperature'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='min_a',
            field=models.FloatField(default=0, verbose_name='min_value_air'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='min_h',
            field=models.FloatField(default=0, verbose_name='min_value_humidity'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='min_t',
            field=models.FloatField(default=0, verbose_name='min_value_temperature'),
        ),
    ]
