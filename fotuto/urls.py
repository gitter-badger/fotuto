from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fotuto.views.home', name='home'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('mimics.urls')),
    url(r'^', include('windows.urls')),
    url(r'^', include('vars.urls')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
