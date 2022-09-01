from django.shortcuts import render
from utils.mixins import AbstractListAPI,AbstractRetrieveAPI,AbstractCreateAPI,AbstractUserRetrieveAPI
from scholarship.serializers import ScholarshipListSerializers,UserScholarshipTaskCreateSerializer,UserScholarshipTaskListSerializer,UserScholarshipTaskVerifySerializer
from django.utils import translation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from account.models  import User
from scholarship.models import UserScholarshipTask
# Create your views here.


class ScholarshipListAPI(AbstractListAPI):
    pagination_class = None
    serializer_class = ScholarshipListSerializers
    

    def get_queryset(self):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return ScholarshipListSerializers.get_query()


class UserScholarshipTaskCreateAPI(AbstractCreateAPI):

    serializer_class = UserScholarshipTaskCreateSerializer

class UserScholarshipTaskListAPI(AbstractListAPI):
    pagination_class = None
    serializer_class = UserScholarshipTaskListSerializer
    

    def get_queryset(self):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return UserScholarshipTaskListSerializer.get_query(self.request.user)



class UserScholarshipTaskVerifyAPI(APIView):

    serializer_class = UserScholarshipTaskVerifySerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.sub_task.id for user in UserScholarshipTask.objects.filter(user=request.user)]
        return Response(usernames)
    
    