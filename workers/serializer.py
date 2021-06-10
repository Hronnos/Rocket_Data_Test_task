from rest_framework import  serializers
from .models import EmployeeMptt


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeMptt
        fields = '__all__'
