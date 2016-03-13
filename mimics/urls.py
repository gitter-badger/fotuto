from django.conf.urls import include, url
from django.views.generic import ListView, CreateView
from rest_framework import routers

from .models import Mimic
from .views import MimicManageView, MimicViewSet

router = routers.DefaultRouter()
router.register(r'mimics', MimicViewSet)

urlpatterns = [
    url(r'^mimics/add/$', CreateView.as_view(model=Mimic), name="mimic_add"),
    url(r'^mimics/$', ListView.as_view(model=Mimic), name="mimic_list"),
    url(r'^windows/(?P<window>[\w-]+)/mimics/manage/$', MimicManageView.as_view(), name="mimic_manage_window"),

    url(r'^api/', include(router.urls)),

]
