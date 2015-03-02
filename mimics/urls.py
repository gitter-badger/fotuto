from django.conf.urls import patterns, include, url
from django.views.generic import ListView, CreateView
from mimics.models import Mimic
from mimics.views import MimicManageView

urlpatterns = patterns('',
    url(r'^mimics/add/$', CreateView.as_view(model=Mimic), name="mimic_add"),
    url(r'^mimics/$', ListView.as_view(model=Mimic), name="mimic_list"),
    url(r'^windows/(?P<window>[\w-]+)/mimics/manage/$', MimicManageView.as_view(), name="mimic_manage_window"),
)