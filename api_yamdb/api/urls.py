from rest_framework import routers
from django.urls import include, path

from .views import CommentViewSet, ReviewViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')
router.register(r'reviews/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments'
                )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
