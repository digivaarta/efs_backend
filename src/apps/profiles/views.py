from django.shortcuts import render
from utils.mixins import AbstractUpdateAPI
from profiles.serializers import UserProfileSerializer
# Create your views here.


class UserProfileAPI(AbstractUpdateAPI):

    serializer_class = UserProfileSerializer