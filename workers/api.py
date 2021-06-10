from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, filters
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import EmployeeMptt


class EmployeeCreateApi(LoginRequiredMixin, generics.CreateAPIView):

    queryset = EmployeeMptt.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeApi(LoginRequiredMixin, generics.ListAPIView):
    search_fields = ['lvl']
    filter_backends = (filters.SearchFilter,)
    queryset = EmployeeMptt.objects.all()
    serializer_class = EmployeeSerializer
