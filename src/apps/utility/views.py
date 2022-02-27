from django.shortcuts import render
from utils.mixins import AbstractRetrieveAPI
from utility.serializers import MetaContentSerializer
# Create your views here.


class MetaContentDetailAPI(AbstractRetrieveAPI):

    serializer_class = MetaContentSerializer

    def get_queryset(self,pk):
        try:
            return MetaContentSerializer.get_query(pk)
        except Exception as e:
            return None



    