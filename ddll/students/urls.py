# coding = utf-8


from django.conf.urls import url
import students.views

urlpatterns = [
    url(r'^$', students.views.index),
    url(r'^login/$', students.views.login),
    url(r'^student_into/$', students.views.student_into),
    url(r'^student_handle/$', students.views.student_handle),
    url(r'^student_view/$', students.views.student_view),
    url(r'^student_view_handle/$', students.views.student_view_handle),
    url(r'^student_alter/$', students.views.student_alter),
    url(r'^student_list/$', students.views.student_list),
    url(r'^student_list_handle/$', students.views.student_list_handle),
]
