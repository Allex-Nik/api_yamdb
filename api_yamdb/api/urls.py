from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import signup, token, UserViewSet, TitleViewSet, CategoryViewSet, GenreViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

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
