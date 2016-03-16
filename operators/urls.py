from rest_framework import routers

from .views import GroupViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
