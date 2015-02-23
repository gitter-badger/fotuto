from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from windows.models import Window
from windows.views import WindowDetailView

urlpatterns = patterns('',
    url(r'^$', WindowDetailView.as_view(), name="mimics"),
    url(r'^windows/add/$', CreateView.as_view(model=Window), name="window_add"),
)