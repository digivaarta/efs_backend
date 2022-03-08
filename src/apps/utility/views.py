from django.shortcuts import render
from utils.mixins import AbstractRetrieveAPI
from django_filters import rest_framework as filters

from utility.serializers import MetaContentSerializer,MetaContentListSerializer
# Create your views here.


class MetaContentDetailAPI(AbstractRetrieveAPI):

    serializer_class = MetaContentSerializer
   

    def get_queryset(self,pk):
        try:
            return MetaContentSerializer.get_query(pk)
        except Exception as e:
            return None


class MetaContentListAPI(AbstractRetrieveAPI):

    serializer_class = MetaContentListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = MetaContentListSerializer.get_query()
    filterset_fields = ('meta_category',)



    