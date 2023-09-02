from django.urls import path
from position.views import PositionViewSet, BrokerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('position', PositionViewSet, basename='user')
router.register('broker', BrokerViewSet, basename='user')
urlpatterns = []
urlpatterns += router.urls
