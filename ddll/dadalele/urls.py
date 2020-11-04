# coding = utf-8


from django.conf.urls import url
import students.views
import dadalele.views

urlpatterns = [
    url(r'^$', students.views.index),
    url(r'^admin/$', dadalele.views.admin),
    url(r'^login/$', dadalele.views.login),
    url(r"^login_handle/$", students.views.login_handle),
    url(r'^student_into/$', students.views.student_into),
    url(r'^student_handle/$', students.views.student_handle),
    url(r'^student_view/$', students.views.student_view),
    url(r'^student_view_handle/$', students.views.student_view_handle),
    url(r'^student_alter/$', students.views.student_alter),
    
    
    url(r'^stu_info_list/$', dadalele.views.stu_info_list),
    url(r'^stu_info_list_handle/$', dadalele.views.stu_info_list_handle),
    url(r'^course_info_list/$', dadalele.views.course_info_list),
    url(r'^class_view/$', dadalele.views.class_view),
    url(r'^stu_info_into/$', dadalele.views.stu_info_into),
    url(r'^stu_info_view/$', dadalele.views.stu_info_view),
    url(r'^stu_info_view_handle/$', dadalele.views.stu_info_view_handle),
    url(r'^stu_info_change/$', dadalele.views.stu_info_change),
    url(r"^student_info_alter/$", students.views.student_info_alter),
    url(r'^course_into/$', dadalele.views.course_into),
    url(r'^course_view/$', dadalele.views.course_view),
    url(r'^course_change/$', dadalele.views.course_change),
    url(r'^class_grouping/$', dadalele.views.class_grouping),
    url(r"^student_add_handle/$", dadalele.views.student_add_handle),
    url(r"^class_list/$", dadalele.views.class_list),
    url(r"^class_into/$", dadalele.views.class_into),
    # url(r'^course_into/$', dadalele.views.course_into),
    # url(r'^course_into/$', dadalele.views.course_into),
    # url(r'^course_into/$', dadalele.views.course_into),


    



    url(r'^student_list_handle/$', students.views.student_list_handle),
    url(r"^student_add/$", students.views.student_add),

]
