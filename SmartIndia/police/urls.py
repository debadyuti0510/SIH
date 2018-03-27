from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
#    url(r'^responseform/$', views.checkresponse, name='checkresponse'),
    url(r'^(?P<phoneno>[0-9]+)/$',views.firdisplay, name='firdisplay')
]
