from django.shortcuts import render
from utils.mixins import AbstractCreateAPI,AbstracLoginAPI,AbstractRetrieveAPI,AbstractUpdateAPI
from rest_framework.permissions import AllowAny

from account.serializer import RegisterSerializer,FcmDeviceSerializer,NewRegisterSerializer,GoogleSignInSerializer,AccountDeactivateSerializer

# Create your views here.


class RegisterViewAPI(AbstractCreateAPI):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class NewRegisterViewAPI(AbstractCreateAPI):

    serializer_class = NewRegisterSerializer
    permission_classes = [AllowAny]

class FCMDeviceViewAPI(AbstractCreateAPI):

    serializer_class = FcmDeviceSerializer  
    permission_classes = [AllowAny]  

class GoogleSignInAPI(AbstractRetrieveAPI):

    serializer_class = GoogleSignInSerializer
    permission_classes = [AllowAny]

    def get_queryset(self,pk):
        return GoogleSignInSerializer.get_query(pk)

class UserDeactivateAPI(AbstractCreateAPI):

    serializer_class = AccountDeactivateSerializer