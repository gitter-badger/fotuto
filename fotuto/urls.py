from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views

from vars.views import DeviceViewSet
from windows.views import WindowViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'windows', WindowViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('windows.urls')),
    url(r'^', include('mimics.urls')),
    url(r'^', include('vars.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
