from django.conf.urls import patterns, include, url
from mimics.views import MimicManageView

urlpatterns = patterns('',
    url(r'^windows/(?P<window>\w+)/mimics/manage/$', MimicManageView.as_view(), name="mimic_add_to_window"),
)