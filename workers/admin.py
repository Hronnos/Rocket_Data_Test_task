from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from workers.models import EmployeeMptt


class EmployeeMpttAdmin(DraggableMPTTAdmin):
    list_display = ('first_name', 'last_name', 'role', 'parent', 'salary', 'paid_out', 'work_start')
    list_filter = ('role', 'lvl')
    list_display_links = ('first_name', 'last_name')

    def delete_paid_out(self, request, queryset):
        queryset.update(paid_out=False)

    actions = [delete_paid_out]


admin.site.register(EmployeeMptt, EmployeeMpttAdmin)
