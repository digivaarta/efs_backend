from urllib import request
from django.shortcuts import render
from django_filters import rest_framework as filters

from utils.mixins import AbstractCreateAPI,AbstractListAPI, AbstractRetrieveAPI,AbstractPKUpdateAPI
from support.serializers import TicketSerializer,SupportSerializer,TicketListSerializer,SupportListSerializer,TicketUpdateSerializer
# Create your views here.



class TicketCreateAPI(AbstractCreateAPI):

    serializer_class = TicketSerializer


class TicketUpdateAPI(AbstractPKUpdateAPI):

    serializer_class = TicketUpdateSerializer

class SupportCreateAPI(AbstractCreateAPI):

    serializer_class = SupportSerializer

class TicketListAPI(AbstractListAPI):

    serializer_class = TicketListSerializer 

    def get_queryset(self):
        return TicketListSerializer.get_query(self.request.user)  


class SupportListAPI(AbstractListAPI):
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = SupportListSerializer
    filterset_fields = ('ticket',)

    def get_queryset(self):
        pk = self.request.GET.get("ticket",None)
        if pk is not None:
            return SupportListSerializer.get_query()
        else:
            return SupportListSerializer.get_none()    

    


    