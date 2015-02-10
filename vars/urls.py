from django.conf.urls import patterns, include, url
from vars.views import VarCreateView

urlpatterns = patterns('',
    url(r'^vars/add/$', VarCreateView.as_view(), name="var_add"),
    url(r'^vars/list/$', VarCreateView.as_view(), name="var_list"),
)