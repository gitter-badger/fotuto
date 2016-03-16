from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views

from windows.views import api_root

urlpatterns = [
    url(r'^api/token/', views.obtain_auth_token, name='api-token'),
    url(r'^api/$', api_root),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('operators.urls')),
    url(r'^', include('windows.urls')),
    url(r'^', include('mimics.urls')),
    url(r'^', include('vars.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
