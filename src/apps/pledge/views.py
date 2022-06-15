from django.shortcuts import render
from utils.mixins import AbstractListAPI,AbstractRetrieveAPI,AbstractCreateAPI,AbstractUserRetrieveAPI
from pledge.serializers import PledgeListSerializer,PledgeDetailSerializer,UserPledgeCreateSerializer
from django.utils import translation

# Create your views here.



class PledgeListAPI(AbstractListAPI):

    serializer_class = PledgeListSerializer
    queryset = PledgeListSerializer.get_query()
    pagination_class = None

class PledgeDetailAPI(AbstractRetrieveAPI):
    serializer_class = PledgeDetailSerializer

    def get_queryset(self,pk):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return PledgeDetailSerializer.get_query(pk)
    
class UserPledgeCreateAPI(AbstractCreateAPI):

    serializer_class = UserPledgeCreateSerializer


class UserPledgeRetrieveAPI(AbstractUserRetrieveAPI):

    serializer_class = UserPledgeCreateSerializer

    def get_queryset(self):
        return UserPledgeCreateSerializer.get_user(self.request.user)
    

    