from django.contrib import admin

from departments.models import Departments
from departments.models import ModelSensor1
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from departments.utils import round_float_to_one

# Register your models here.
admin.site.register(Departments)



class Sensors(resources.ModelResource):

    class Meta:
        model = ModelSensor1




class SensorAdmin(ImportExportActionModelAdmin):
    sensor_class = Sensors
    list_display = [field.name for field in ModelSensor1._meta.fields]


admin.site.register(ModelSensor1,SensorAdmin)