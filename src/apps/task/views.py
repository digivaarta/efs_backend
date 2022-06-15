from django.shortcuts import render
from utils.mixins import AbstractListAPI,AbstractCreateAPI,AbstractRetrieveAPI
from task.serializers import TaskListSerializer,UserTaskCreateSerializer,UserTaskListSerializer,UserTaskStatusSerializer
# Create your views here.
from django.utils import translation


class TaskListAPI(AbstractListAPI):

    serializer_class = TaskListSerializer
    pagination_class = None
    queryset = TaskListSerializer.get_query()

    def get_queryset(self):
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return TaskListSerializer.get_query()
    

class UserTaskCreateAPI(AbstractCreateAPI):

    serializer_class = UserTaskCreateSerializer


class UserTaskListAPI(AbstractListAPI):

    serializer_class = UserTaskListSerializer
    pagination_class = None
    

    def get_queryset(self):
        return UserTaskListSerializer.get_query(self.request.user)
     
class UserTaskStatusAPI(AbstractRetrieveAPI):

    serializer_class =  UserTaskStatusSerializer

    def get_queryset(self,pk):
        user = self.request.user
        return UserTaskStatusSerializer.get_object(pk,user)

        
         