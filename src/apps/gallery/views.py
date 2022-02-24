from django.shortcuts import render
from apps.banners.serializers import BannerSerializer
from utils.mixins import AbstractListAPI
from gallery.serializers import GallerySerializer
# Create your views here.


class GalleryListAPI(AbstractListAPI):
    pagination_class = None
    serializer_class = GallerySerializer
    queryset = GallerySerializer.get_query()

