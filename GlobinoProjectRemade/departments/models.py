from django.db import models


# Create your models here.

class Departments(models.Model):
    title = models.CharField('Name',max_length=20)
    description = models.TextField('Description')

    min_t = models.FloatField('min_value_temperature',default = 0)
    max_t = models.FloatField('max_value_temperature',default = 1)
    default_value_t = models.FloatField('default_value_temperature',default=1)

    min_h = models.FloatField('min_value_humidity',default = 0)
    max_h = models.FloatField('max_value_humidity',default = 1)
    default_value_h = models.FloatField('default_value_humidity',default=1)

    min_a = models.FloatField('min_value_air',default = 0)
    max_a = models.FloatField('max_value_air',default = 1)
    default_value_a = models.FloatField('default_value_air',default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/departments/{self.id}'

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

class ModelSensor1(models.Model):
    department_id = models.IntegerField('department_id',default = 0)
    temperature = models.FloatField('temperature', default = 0)
    humidity = models.FloatField('humidity ', default = 1 )
    air_currents = models.FloatField('air_currents', default= 1 )

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'
