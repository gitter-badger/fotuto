from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from vars.models import Device, Var
from vars.views import VarCreateView, DeviceCreateView

urlpatterns = patterns('',
    url(r'^vars/add/$', VarCreateView.as_view(), name="var_add"),
    url(r'^vars/$', ListView.as_view(model=Var), name="var_list"),

    url(r'^devices/add/$', DeviceCreateView.as_view(), name="device_add"),
    url(r'^devices/$', ListView.as_view(model=Device), name="device_list"),
)