from django.urls import include, path

from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()
comments_router = SimpleRouter()

ads_router.register("", AdViewSet, basename="ads")
comments_router.register("comments", CommentViewSet, basename='comments')

urlpatterns = [
    path("", include(ads_router.urls)),
    path("<int:ad>/", include(comments_router.urls)),
]
