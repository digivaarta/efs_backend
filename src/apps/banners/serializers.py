from rest_framework import serializers
from pledge.models import UserPledge

from banners.models import Banner


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        exclude = ("user",)

    @classmethod
    def get_query(cls):
        return Banner.objects.filter(is_active=True)   


class PledgeCountSerializer(serializers.Serializer):

    count = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"

    @classmethod
    def get_empty_none(self):
        return UserPledge.objects.none()

    def get_count(self,obj):
        return UserPledge.objects.all().count()
