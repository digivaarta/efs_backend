from django.shortcuts import render
from utils.mixins import AbstractRetrieveAPI
from django_filters import rest_framework as filters

from utility.serializers import MetaContentSerializer
# Create your views here.


class MetaContentDetailAPI(AbstractRetrieveAPI):

    serializer_class = MetaContentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('meta_category',)

    def get_queryset(self,pk):
        try:
            return MetaContentSerializer.get_query(pk)
        except Exception as e:
            return None



    