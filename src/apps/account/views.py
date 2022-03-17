from django.shortcuts import render
from utils.mixins import AbstractCreateAPI,AbstracLoginAPI
from rest_framework.permissions import AllowAny

from account.serializer import RegisterSerializer,FcmDeviceSerializer

# Create your views here.


class RegisterViewAPI(AbstractCreateAPI):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class FCMDeviceViewAPI(AbstractCreateAPI):

    serializer_class = FcmDeviceSerializer  
    permission_classes = [AllowAny]  
    