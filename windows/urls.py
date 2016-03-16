from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from rest_framework import routers

from .models import Window
from .views import WindowDetailView, WindowCreateView, WindowDefaultView, WindowViewSet, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^$', WindowDefaultView.as_view(), name="mimics"),
    url(r'^windows/add/$', WindowCreateView.as_view(), name="window_add"),
    url(r'^windows/(?P<slug>[\w-]+)/$', WindowDetailView.as_view(), name="window_details"),
    # TODO: Take aware that view can't be named 'add' to avoid url conflicts
    url(r'^windows/$', ListView.as_view(model=Window), name="window_list"),
]
