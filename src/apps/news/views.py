from django.shortcuts import render
from apps.banners.serializers import BannerSerializer
from utils.mixins import AbstractListAPI
from news.serializers import NewsSerializer
from django_filters import rest_framework as filters
from django.utils import translation

# Create your views here.


class NewsListAPI(AbstractListAPI):
    
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('news_type',)

    def get_queryset(self):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return NewsSerializer.get_query() 



