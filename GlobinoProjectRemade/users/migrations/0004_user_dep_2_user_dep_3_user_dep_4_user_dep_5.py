# Generated by Django 4.2 on 2023-05-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_dep_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dep_2',
            field=models.CharField(default='No', max_length=3, verbose_name='dep_2'),
        ),
        migrations.AddField(
            model_name='user',
            name='dep_3',
            field=models.CharField(default='No', max_length=3, verbose_name='dep_3'),
        ),
        migrations.AddField(
            model_name='user',
            name='dep_4',
            field=models.CharField(default='No', max_length=3, verbose_name='dep_4'),
        ),
        migrations.AddField(
            model_name='user',
            name='dep_5',
            field=models.CharField(default='No', max_length=3, verbose_name='dep_5'),
        ),
    ]
