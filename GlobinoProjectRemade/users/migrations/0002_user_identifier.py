# Generated by Django 4.2 on 2023-05-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identifier',
            field=models.CharField(default='', max_length=40, verbose_name='id'),
        ),
    ]
