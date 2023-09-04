from django.urls import path
from position.views import PositionViewSet, BrokerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('position', PositionViewSet, basename='position')
router.register('broker', BrokerViewSet, basename='broker')
urlpatterns = []
urlpatterns += router.urls
