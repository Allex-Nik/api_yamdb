from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, signup, token

router = DefaultRouter()

router.register('v1/users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', token),
]
