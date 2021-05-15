from core.models import Thumbnail
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from thumbnails.serializers import (
    BasicThumbnailSerializer,
    EnterpriseThumbnailSerializer,
    PremiumThumbnailSerializer,
    ThumbnailListSerializer
)


class ThumbnailViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Thumbnail.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action in ('list', 'upload_image'):
            return ThumbnailListSerializer
        if self.request.user.plan.id == 'P':
            return PremiumThumbnailSerializer
        if self.request.user.plan.id == 'E':
            return EnterpriseThumbnailSerializer
        return BasicThumbnailSerializer

    @action(methods=('post',), detail=True)
    def upload_image(self, request, pk=None):
        image = self.get_object()
        serializer = self.get_serializer(
            image,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
