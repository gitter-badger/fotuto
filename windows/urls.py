from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from windows.views import WindowDetailView

urlpatterns = patterns('',
    url(r'^$', WindowDetailView.as_view(), name="mimics"),
    url(r'^windows/add/$', CreateView.as_view(), name="window_add"),
)