from django.shortcuts import render
from apps.banners.serializers import BannerSerializer
from utils.mixins import AbstractListAPI
from banners.serializers import BannerSerializer
# Create your views here.


class BannerListAPI(AbstractListAPI):
    pagination_class = None
    serializer_class = BannerSerializer
    queryset = BannerSerializer.get_query()

