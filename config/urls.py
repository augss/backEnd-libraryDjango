from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet, CategoryViewSet, PublisherViewSet

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"publishers", PublisherViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]