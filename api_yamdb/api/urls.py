from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import signup, token, UserViewSet, TitleViewSet, CategoryViewSet, GenreViewSet, CommentViewSet, ReviewViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')


router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, 
    basename='comments'
)

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
