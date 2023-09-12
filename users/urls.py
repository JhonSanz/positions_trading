from django.urls import path
from users.views.user import UserViewSet
from rest_framework.routers import DefaultRouter
from users.views.authentication import CustomTokenObtainPairView, Logout

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', Logout.as_view(), name='logout'),
]
urlpatterns += router.urls
