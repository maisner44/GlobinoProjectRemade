import base64
from typing import io

from django.core.mail import send_mail
from django.shortcuts import render,redirect
from departments.models import Departments
from departments.models import ModelSensor1
from departments.forms import DepartmentsForm
from django.http import JsonResponse, HttpResponse
from departments.jobs import get_current_sensor_value
from django.views.generic import DetailView,UpdateView
import matplotlib.pyplot as plt



class DepUpdateView(UpdateView):
    model = Departments
    template_name = 'create.html'
    form_class = DepartmentsForm

class DepDetailView(DetailView):
    model = Departments
    template_name = 'dep_detail.html'
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.get_object()
        # Получаем все объекты ModelSensor, связанные с текущим отделом
        sensors = ModelSensor1.objects.filter(department_id=department.id)
        point = get_current_sensor_value()
        context['point'] = point
        sensors = sensors[point]
        context['random_sensor'] = sensors




        return context




def sensor_list(request):
    sensors = ModelSensor1.objects.all()
    return sensors

def departments_home(request):
    departments = Departments.objects.all()
    return render(request, 'dep_choose.html', {'departments':departments})

def create(request):
    error = ''
    if request.method == 'POST':
        form = DepartmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            error = 'fill form properly!'




    form = DepartmentsForm()

    data = {
        'form':form
    }
    return render(request,'create.html',data)

