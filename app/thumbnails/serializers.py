from rest_framework import serializers

from core.models import Thumbnail
from thumbnails.utils import generate_thumbnail


class ThumbnailListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = ('name', 'image')


class BasicThumbnailSerializer(serializers.ModelSerializer):
    small = serializers.SerializerMethodField()

    def get_small(self):
        return generate_thumbnail(self.image, 200)

    class Meta:
        model = Thumbnail
        fields = ('small',)


class PremiumThumbnailSerializer(BasicThumbnailSerializer):
    medium = serializers.SerializerMethodField()

    def get_medium(self):
        return generate_thumbnail(self.image, 400)

    class Meta(BasicThumbnailSerializer.Meta):
        fields = BasicThumbnailSerializer.Meta.fields + ('medium', 'image')


class EnterpriseThumbnailSerializer(PremiumThumbnailSerializer):
    timed = serializers.SerializerMethodField()

    class Meta(PremiumThumbnailSerializer.Meta):
        fields = PremiumThumbnailSerializer.Meta.fields + ('timed',)
