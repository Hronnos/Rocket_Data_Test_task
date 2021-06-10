import mptt
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class EmployeeMptt(MPTTModel):
    STANDARD = 'STD'
    TECHNICIAN = 'TECH'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (TECHNICIAN, 'technician'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president'))

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES, verbose_name="Должность")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    work_start = models.DateTimeField(default=timezone.now, verbose_name="Начало работы")
    salary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Заработная плата")
    paid_out = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Выплаченная зарплата", blank=True, null=True)
    lvl = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True, verbose_name="Уровень")
    parent = TreeForeignKey('self', null=True, related_name='children', on_delete=models.CASCADE, blank=True, verbose_name="Начальник")

    def __unicode__(self):
        return self.role

    def __str__(self):
        return self.role

    class MPTTMeta:
        parent_attr = 'parent'


mptt.register(EmployeeMptt, order_insertion_py=['role'])

