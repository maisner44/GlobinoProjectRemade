from django.conf import settings
import requests
import json
from django.shortcuts import render
import random
from departments.models import Departments
from departments.models import ModelSensor1
from django.core.mail import send_mail
from users.models import User
import datetime
emails = User.objects.filter(send_message='Y').values_list('email', flat=True)
model = Departments
sensors1 = ModelSensor1.objects.filter(department_id=1)
sensors2 = ModelSensor1.objects.filter(department_id=2)
sensors3 = ModelSensor1.objects.filter(department_id=3)
sensors4 = ModelSensor1.objects.filter(department_id=4)
sensors5 = ModelSensor1.objects.filter(department_id=5)
department1 = Departments.objects.get(id = 1)
department2 = Departments.objects.get(id = 2)
department3 = Departments.objects.get(id = 3)
department4 = Departments.objects.get(id = 4)
department5 = Departments.objects.get(id = 5)

current_sensor_value = 0

def get_current_sensor_value():
    global current_sensor_value
    return current_sensor_value

def schedule_api_random():
    rand = random.randint(0, 49)
    global current_sensor_value
    current_sensor_value = rand
    return rand

def schedule_api():
    point1 = schedule_api_random()
    sensors_1 = sensors1[point1]
    sensors_2 = sensors2[point1]
    sensors_3 = sensors3[point1]
    sensors_4 = sensors4[point1]
    sensors_5 = sensors5[point1]

    if sensors_1.temperature < float(department1.min_t) or sensors_1.temperature > float(department1.max_t):
        send_mail(
            'Hi',
            f'Увага!В Department {1} Показники температури не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_1.humidity < float(department1.min_h) or sensors_1.humidity > float(department1.max_h):
        send_mail(
            'Hi',
            f'Увага!В Department {1} Показники вологості не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_1.air_currents < float(department1.min_a) or sensors_1.air_currents > float(department1.max_a):
        send_mail(
            'Hi',
            f'Увага!В Department {1} Показники повітряних потоків не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )



    if sensors_2.temperature < float(department2.min_t) or sensors_2.temperature > float(department2.max_t):
        send_mail(
            'Hi',
            f'Увага!В Department {2} Показники температури не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_2.humidity < float(department2.min_h) or sensors_2.humidity > float(department2.max_h):
        send_mail(
            'Hi',
            f'Увага!В Department {2} Показники вологості не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_2.air_currents < float(department2.min_a) or sensors_2.air_currents > float(department2.max_a):
        send_mail(
            'Hi',
            f'Увага!В Department {2} Показники повітряних потоків не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )



    if sensors_3.temperature < float(department3.min_t) or sensors_3.temperature > float(department3.max_t):
        send_mail(
            'Hi',
            f'Увага!В Department {3} Показники температури не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_3.humidity < float(department3.min_h) or sensors_3.humidity > float(department3.max_h):
        send_mail(
            'Hi',
            f'Увага!В Department {3} Показники вологості не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_3.air_currents < float(department3.min_a) or sensors_3.air_currents > float(department3.max_a):
        send_mail(
            'Hi',
            f'Увага!В Department {3} Показники повітряних потоків не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )



    if sensors_4.temperature < float(department4.min_t) or sensors_4.temperature > float(department4.max_t):
        send_mail(
            'Hi',
            f'Увага!В Department {4} Показники температури не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_4.humidity < float(department4.min_h) or sensors_4.humidity > float(department4.max_h):
        send_mail(
            'Hi',
            f'Увага!В Department {4} Показники вологості не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_4.air_currents < float(department4.min_a) or sensors_4.air_currents > float(department4.max_a):
        send_mail(
            'Hi',
            f'Увага!В Department {4} Показники повітряних потоків не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )




    if sensors_5.temperature < float(department5.min_t) or sensors_5.temperature > float(department5.max_t):
        send_mail(
            'Hi',
            f'Увага!В Department {5} Показники температури не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_5.humidity < float(department5.min_h) or sensors_5.humidity > float(department5.max_h):
        send_mail(
            'Hi',
            f'Увага!В Department {5} Показники вологості не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )

    if sensors_5.air_currents < float(department5.min_a) or sensors_5.air_currents > float(department5.max_a):
        send_mail(
            'Hi',
            f'Увага!В Department {5} Показники повітряних потоків не відповідають нормам. Відбувається налагодження режиму',
            'globinosensors@gmail.com',
            emails,
            fail_silently=False,
        )
    now = datetime.datetime.now()

    print(f'Оновлення та перевіка даних,random sensor: {point1},time: {now},current_sensor_value {current_sensor_value }')

    return point1




