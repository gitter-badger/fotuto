from django.conf.urls import patterns, include, url
from windows.views import WindowDetailView

urlpatterns = patterns('',
    url(r'^$', WindowDetailView.as_view(), name="mimics"),
)