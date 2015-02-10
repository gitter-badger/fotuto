from django.conf.urls import patterns, include, url
from vars.views import VarCreateView

urlpatterns = patterns('',
    url(r'^add/$', VarCreateView.as_view(), name="mimics"),
)