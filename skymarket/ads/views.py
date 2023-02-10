from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.filters import AdTitleFilter
from ads.models import Ad, Comment
from ads.permissions import CustomAdPermission, CustomCommentPermission
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdTitleFilter
    pagination_class = AdPagination

    def get_serializer_class(self):
        if self.action == "list":
            return AdSerializer
        return AdDetailSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        image = self.kwargs.get("image")
        serializer.save(author=current_user, image=image if image else None)

    @action(detail=False, methods=['get'], permission_classes=[CustomAdPermission])
    def me(self, request):
        my_ads = Ad.objects.filter(author=self.request.user).all()
        page = self.paginate_queryset(my_ads)
        serializer = AdSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, CustomAdPermission]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, CustomCommentPermission,)

    def get_queryset(self):
        ad = self.kwargs.get("ad")
        if ad:
            return Comment.objects.filter(ad=ad)
        return super().get_queryset()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs.get("ad"))
        serializer.save(ad=ad, author=self.request.user)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return self.object
