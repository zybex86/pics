from django.urls import include, path
from rest_framework.routers import DefaultRouter

from thumbnails.views import ThumbnailViewSet


router = DefaultRouter()
router.register('links', ThumbnailViewSet, basename='link')

app_name = 'thumbnails'

urlpatterns = [
    path('', include(router.urls))
]
