from django.shortcuts import render
from apps.banners.serializers import BannerSerializer
from utils.mixins import AbstractListAPI
from banners.serializers import BannerSerializer,PledgeCountSerializer
from rest_framework import views
from rest_framework.response import Response
from django.utils import translation

# Create your views here.


class BannerListAPI(AbstractListAPI):
    pagination_class = None
    serializer_class = BannerSerializer
    

    def get_queryset(self):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return BannerSerializer.get_query() 





class PledgeCountAPI(views.APIView):
    pagination_class = None

    def get(self,request):
        context = {"request":request}
        empty = PledgeCountSerializer.get_empty_none
        result = PledgeCountSerializer(empty,context=context).data
        return Response(result)