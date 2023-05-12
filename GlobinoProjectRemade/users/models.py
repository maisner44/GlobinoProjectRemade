from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    identifier = models.CharField('id',max_length=40, default = '')
    dep_1 = models.CharField('dep_1', max_length=3, default='N')
    dep_2 = models.CharField('dep_2', max_length=3, default='N')
    dep_3 = models.CharField('dep_3', max_length=3, default='N')
    dep_4 = models.CharField('dep_4', max_length=3, default='N')
    dep_5 = models.CharField('dep_5', max_length=3, default='N')
    update_permission = models.CharField('update_permission', max_length=3, default='N')
    send_message = models.CharField('send_message', max_length=3, default='N')

