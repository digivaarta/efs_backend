from django.shortcuts import render
from utils.mixins import AbstractListAPI,AbstractRetrieveAPI,AbstractCreateAPI,AbstractUserRetrieveAPI
from scholarship.serializers import ScholarshipListSerializers,UserScholarshipTaskCreateSerializer,UserScholarshipTaskListSerializer
from django.utils import translation

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
