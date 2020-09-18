from django.contrib import admin
from students.models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['t_name', 't_age']


admin.site.register(StudentInfo)
admin.site.register(CourseInfo)
admin.site.register(TeacherInfo, TeacherAdmin)
admin.site.register(MoneyInfo)
admin.site.register(ClassInfo)
admin.site.register(StudentClassInfo)





# Register your models here.
