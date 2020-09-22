from django.contrib import admin
from students.models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['t_name', 't_age']
    search_fields = ['t_name']
    list_per_page = 10
    list_filter = ['t_name']
    actions_on_top = True
    actions_on_bottom = True

class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_id', 's_birthday', 's_into']
    search_fields = ['s_name', 's_id', 's_birthday', 's_into']
    list_per_page = 10
    list_filter = ['isDelete']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_course_id', 'c_section_theme']
    search_fields = ['c_section_theme']
    list_per_page = 10
    list_filter = ['c_course_id', 'c_section_theme']


class MoneyAdmin(admin.ModelAdmin):
    list_display = ['m_id', 'm_money']
    search_fields = ['m_id']
    list_per_page = 10
    list_filter = ['m_id', 'm_money']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['cl_id', 'cl_name']
    search_fields = ['cl_name']
    list_per_page = 10
    list_filter = ['cl_id', 'cl_name']


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['kc_id', 'sc_section_theme', 'sc_date']
    search_fields = ['kc_id', 'sc_section_theme', 'sc_date']
    list_per_page = 10
    list_filter = ['kc_id']


class ClassDetailInfoAdmin(admin.ModelAdmin):
    list_display = ['kcls_id_id', 's_id_id', 'cd_note']
    search_fields = ['kcls_id_id', 's_id_id', 'cd_note']
    list_per_page = 10
    list_filter = ['kcls_id_id']


admin.site.register(StudentInfo, StudentAdmin)
admin.site.register(CourseInfo, CourseAdmin)
admin.site.register(TeacherInfo, TeacherAdmin)
admin.site.register(MoneyInfo, MoneyAdmin)
admin.site.register(ClassInfo, ClassAdmin)
admin.site.register(StudentClassInfo,StudentClassAdmin)
admin.site.register(ClassDetailInfo, ClassDetailInfoAdmin)




# Register your models here.
