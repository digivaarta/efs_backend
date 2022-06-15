from django.shortcuts import render
from utils.mixins import AbstractUpdateAPI,AbstractCreateAPI
from profiles.serializers import UserProfileSerializer,UserOTPSerializer
# Create your views here.


class UserProfileAPI(AbstractUpdateAPI):

    serializer_class = UserProfileSerializer

class UserOtpAPI(AbstractCreateAPI):

    serializer_class = UserOTPSerializer    