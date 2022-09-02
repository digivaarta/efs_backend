from django.shortcuts import render
from utils.mixins import AbstractRetrieveAPI,AbstractListAPI,AbstractCreateAPI
from django_filters import rest_framework as filters

from utility.serializers import MetaContentSerializer,MetaContentListSerializer,SuggestionSerializer
# Create your views here.
from django.utils import translation



class MetaContentDetailAPI(AbstractRetrieveAPI):

    serializer_class = MetaContentSerializer
   

    def get_queryset(self,pk):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        try:
            return MetaContentSerializer.get_query(pk)
        except Exception as e:
            return None


class MetaContentListAPI(AbstractListAPI):

    serializer_class = MetaContentListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    
    filterset_fields = ('meta_category',)
    pagination_class = None

    def get_queryset(self):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return MetaContentListSerializer.get_query() 


class SuggestionCreateAPI(AbstractCreateAPI):

    serializer_class = SuggestionSerializer
    