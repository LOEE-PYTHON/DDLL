from django.contrib import admin
from students.models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['t_name', 't_age']
    search_fields = ['t_name']
    list_per_page = 10
    list_filter = ['t_name']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('t_name', 't_age')




class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_id', 's_birthday', 's_into']
    search_fields = ['s_name', 's_id', 's_birthday', 's_into']
    list_per_page = 10
    list_filter = ['isDelete']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('s_name', 's_id', 's_birthday', 's_into')
    # 详细时间分层筛选
    date_hierarchy = 's_birthday'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_course_id', 'c_section_theme']
    search_fields = ['c_section_theme']
    list_per_page = 10
    list_filter = ['c_section_theme']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('c_course_id', 'c_section_theme')


class MoneyAdmin(admin.ModelAdmin):
    list_display = ['m_id', 'm_money']
    search_fields = ['m_id']
    list_per_page = 10
    list_filter = ['m_id', 'm_money']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('m_id', 'm_money')


class ClassAdmin(admin.ModelAdmin):
    list_display = ['cl_id', 'cl_name']
    search_fields = ['cl_name']
    list_per_page = 10
    list_filter = ['cl_id', 'cl_name']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('cl_id', 'cl_name')


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['sc_id', 'sc_teacher_name', 'sc_section_theme', 'sc_date']
    search_fields = ['sc_id', 'sc_teacher_name', 'sc_section_theme', 'sc_date']
    list_per_page = 10
    list_filter = ['sc_teacher_name']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('sc_id', 'sc_teacher_name', 'sc_section_theme', 'sc_date')
    # fk_fields 设置显示外键字段
    fk_fields = ('publish_id',)


class ClassDetailInfoAdmin(admin.ModelAdmin):
    list_display = ['c_id', 's_id', 't_name', 'cd_note']
    search_fields = ['c_id', 's_id', 't_name','cd_note']
    list_per_page = 10
    list_filter = ['t_name']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('c_id', 's_id', 't_name', 'cd_note')


class ClassUserInfoAdmin(admin.ModelAdmin):
    list_display = ['u_name', 'u_pwd', 'u_type', 'u_nickname']
    search_fields = ['u_name', 'u_pwd', 'u_type', 'u_nickname']
    list_per_page = 10
    list_filter = ['u_name']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('u_name', 'u_pwd', 'u_type', 'u_nickname')


class CourseTypeInfoAdmin(admin.ModelAdmin):
    list_display = ['ct_course_id', 'ct_course_name','ct_study_age','ct_equipment']
    search_fields = ['ct_course_id', 'ct_course_name','ct_study_age','ct_equipment']
    list_per_page = 10
    list_filter = ['ct_course_name']
    actions_on_top = True
    actions_on_bottom = True
    # 设置其他字段也可以点击链接进入编辑界面。
    list_display_links = ('ct_course_id', 'ct_course_name','ct_study_age','ct_equipment')


admin.site.register(StudentInfo, StudentAdmin)
admin.site.register(CourseInfo, CourseAdmin)
admin.site.register(TeacherInfo, TeacherAdmin)
admin.site.register(MoneyInfo, MoneyAdmin)
admin.site.register(ClassInfo, ClassAdmin)
admin.site.register(StudentClassInfo, StudentClassAdmin)
admin.site.register(ClassDetailInfo, ClassDetailInfoAdmin)
admin.site.register(CourseTypeInfo, CourseTypeInfoAdmin)
admin.site.register(UserInfo, ClassUserInfoAdmin)
admin.site.site_title = "搭搭乐乐管理系统"
admin.site.site_header = "搭搭乐乐管理系统"


# Register your models here.
