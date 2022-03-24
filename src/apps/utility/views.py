from django.shortcuts import render
from utils.mixins import AbstractRetrieveAPI,AbstractListAPI,AbstractCreateAPI
from django_filters import rest_framework as filters

from utility.serializers import MetaContentSerializer,MetaContentListSerializer,SuggestionSerializer
# Create your views here.


class MetaContentDetailAPI(AbstractRetrieveAPI):

    serializer_class = MetaContentSerializer
   

    def get_queryset(self,pk):
        try:
            return MetaContentSerializer.get_query(pk)
        except Exception as e:
            return None


class MetaContentListAPI(AbstractListAPI):

    serializer_class = MetaContentListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = MetaContentListSerializer.get_query()
    filterset_fields = ('meta_category',)
    pagination_class = None


class SuggestionCreateAPI(AbstractCreateAPI):

    serializer_class = SuggestionSerializer
    