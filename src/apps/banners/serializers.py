from rest_framework import serializers

from banners.models import Banner


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        exclude = ("user",)

    @classmethod
    def get_query(cls):
        return Banner.objects.filter(is_active=True)   