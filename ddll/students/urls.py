# coding = utf-8


from django.conf.urls import url
import students.views

urlpatterns = [
    url(r'^$', students.views.index),
    url(r'^login/$', students.views.login),
    url(r'^student_into/$', students.views.student_into),
    url(r'^student_handle/$', students.views.student_handle),
    url(r'^student_query/$', students.views.student_query),
    url(r'^student_show/$', students.views.student_show),
]
