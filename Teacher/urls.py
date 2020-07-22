from rest_framework import routers
from .api import FYPViewSet, StudentViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('api/record', StudentViewSet, 'record')
router.register('api/adminrecord', FYPViewSet, 'adminrecord')

urlpatterns = router.urls
