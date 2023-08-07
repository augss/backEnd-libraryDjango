from django.contrib import admin
from django.urls import include, path

from user.router import router as user_router


from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet, CategoryViewSet, PublisherViewSet

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"publishers", PublisherViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(user_router.urls)),

]