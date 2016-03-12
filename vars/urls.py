from django.conf.urls import include, url
from django.views.generic import ListView
from rest_framework import routers

from vars.models import Device, Var
from vars.views import VarCreateView, DeviceCreateView, DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    url(r'^vars/add/$', VarCreateView.as_view(), name="var_add"),
    url(r'^vars/$', ListView.as_view(model=Var), name="var_list"),

    url(r'^devices/add/$', DeviceCreateView.as_view(), name="device_add"),
    url(r'^devices/$', ListView.as_view(model=Device), name="device_list"),
    url(r'^api/', include(router.urls)),

]