from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from vars.models import Device
from vars.views import VarCreateView

urlpatterns = patterns('',
    url(r'^vars/add/$', VarCreateView.as_view(), name="var_add"),
    url(r'^vars/list/$', VarCreateView.as_view(), name="var_list"),

    url(r'^devices/add/$', CreateView.as_view(model=Device), name="device_add"),
)