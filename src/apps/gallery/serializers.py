from rest_framework import serializers

from gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        exclude = ("user",)

    @classmethod
    def get_query(cls):
        return Gallery.objects.filter(is_active=True)   