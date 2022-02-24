from django.shortcuts import render
from apps.banners.serializers import BannerSerializer
from utils.mixins import AbstractListAPI
from news.serializers import NewsSerializer
from django_filters import rest_framework as filters

# Create your views here.


class NewsListAPI(AbstractListAPI):
    
    serializer_class = NewsSerializer
    queryset = NewsSerializer.get_query()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('news_type',)

