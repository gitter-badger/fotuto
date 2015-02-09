from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isuscada.views.home', name='home'),
    url(r'^', include('windows.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
