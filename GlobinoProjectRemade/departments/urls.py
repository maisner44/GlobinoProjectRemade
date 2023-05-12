from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .import views




urlpatterns = [
    path('',views.departments_home,name = 'departments_home'),
    path('create/',views.create,name = 'create'),
    path('<int:pk>',views.DepDetailView.as_view(),name = 'dep_detail'),
    path('<int:pk>/update',views.DepUpdateView.as_view(),name = 'dep_update'),

]