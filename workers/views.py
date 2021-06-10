from django.shortcuts import render
from .models import EmployeeMptt


def index(request):
    employees = EmployeeMptt.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'employee/index.html', context)
