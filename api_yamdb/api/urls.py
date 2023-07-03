from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import signup, token, UserViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)

auth_urls = [
    path('auth/signup/', signup, name='signup'),
    path('auth/token/', token, name='token')
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(auth_urls)),
]
