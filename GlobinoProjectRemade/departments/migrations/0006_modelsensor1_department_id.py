# Generated by Django 4.2 on 2023-05-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0005_modelsensor1_delete_modelsensor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelsensor1',
            name='department_id',
            field=models.IntegerField(default=0, verbose_name='department_id'),
        ),
    ]