from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from vars.forms import DeviceForm
from vars.models import Device
from vars.views import VarCreateView

urlpatterns = patterns('',
    url(r'^vars/add/$', VarCreateView.as_view(), name="var_add"),
    url(r'^vars/$', VarCreateView.as_view(), name="var_list"),

    url(r'^devices/add/$', CreateView.as_view(model=Device, form_class=DeviceForm, success_url=reverse_lazy('device_list')), name="device_add"),
    url(r'^devices/$', ListView.as_view(model=Device), name="device_list"),
)