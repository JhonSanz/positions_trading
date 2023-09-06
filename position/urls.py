from django.urls import path
from position.views.position import PositionViewSet
from position.views.broker import BrokerViewSet
from position.views.money import MoneyViewSet
from position.views.account import AccountViewSet
from position.views.asset import AssetViewSet
from position.views.accountmoney import AccountMoneyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('position', PositionViewSet, basename='position')
router.register('broker', BrokerViewSet, basename='broker')
router.register('money', MoneyViewSet, basename='money')
router.register('account', AccountViewSet, basename='account')
router.register('asset', AssetViewSet, basename='asset')
router.register('accountmoney', AccountMoneyViewSet, basename='accountmoney')

urlpatterns = []
urlpatterns += router.urls
