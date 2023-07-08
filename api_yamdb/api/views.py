import random

from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets, mixins
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response

from .filters import TitleFilter
from .permissions import (Admin,
                          AdminOrReadOnly,
                          ReviewPermission)
from .serializers import (SignupSerializer,
                          TokenSerializer,
                          UserSerializer,
                          TitleSerializer,
                          CategorySerializer,
                          GenreSerializer,
                          CommentSerializer,
                          ReviewSerializer,
                          TitleSerializerRead,
                          TitleSerializerCreate)
from users.models import User
from reviews.models import Title, Category, Genre, Review


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (Admin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'
    http_method_names = ('get', 'post', 'patch', 'delete',)

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        url_path='me',
        permission_classes=[IsAuthenticated]
    )
    def me_page(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = UserSerializer(
                request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(role=request.user.role)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@permission_classes((AllowAny,))
def signup(request):
    username = request.data.get('username')
    if User.objects.filter(username=username).exists():
        user = get_object_or_404(User, username=username)
        serializer = SignupSerializer(
            user, data=request.data, partial=True
        )
        serializer.is_valid()
        if serializer.validated_data['email'] != user.email:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        send_confirmation_code(username)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    send_confirmation_code(username)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def token(request):
    serializer = TokenSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        user = get_object_or_404(User, username=username)
        access = AccessToken.for_user(user)
        return Response(f'token: {access}', status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_confirmation_code(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = int(
        ''.join([str(random.randrange(0, 10))
                 for _ in range(16)])
    )
    user.confirmation_code = confirmation_code
    send_mail(
        'Код подтвержения Yamdb',
        f'Ваш код подтвержения: {user.confirmation_code}',
        'admin@yamdb.com',
        (user.email,),
        fail_silently=False,
    )
    user.save()


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'DELETE',):
            return TitleSerializerCreate
        return TitleSerializerRead


class ExcludeRetrieveUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryViewSet(ExcludeRetrieveUpdateViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ExcludeRetrieveUpdateViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (ReviewPermission,)
    pagination_class = LimitOffsetPagination

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get("title_id"))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())

    def get_queryset(self):
        return self.get_title().reviews.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (ReviewPermission,)
    pagination_class = LimitOffsetPagination

    def get_review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())

    def get_queryset(self):
        return self.get_review().comments.all()
