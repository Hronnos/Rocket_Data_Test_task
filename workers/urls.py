from django.urls import path, include
from .api import EmployeeCreateApi, EmployeeApi
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/create', EmployeeCreateApi.as_view()),
    path('api', EmployeeApi.as_view()),
]
