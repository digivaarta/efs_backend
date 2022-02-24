from django.shortcuts import render
from utils.mixins import AbstractCreateAPI,AbstracLoginAPI

from account.serializer import RegisterSerializer,FcmDeviceSerializer

# Create your views here.


class RegisterViewAPI(AbstractCreateAPI):

    serializer_class = RegisterSerializer

class FCMDeviceViewAPI(AbstractCreateAPI):

    serializer_class = FcmDeviceSerializer    
    