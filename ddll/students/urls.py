# coding = utf-8


from django.conf.urls import url
import students.views

urlpatterns = [
    url(r'^$', students.views.index),
]
