from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pics.uploader.views import ThumbnailViewSet


router = DefaultRouter()
router.register(r'thumbnails', ThumbnailViewSet)

urlpatterns = [
    path('', include(router.urls))
]
