# Generated by Django 4.2 on 2023-05-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dep_1',
            field=models.CharField(default='No', max_length=3, verbose_name='dep_1'),
        ),
    ]
