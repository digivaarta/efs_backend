from django.shortcuts import render
from utils.mixins import AbstractListAPI,AbstractCreateAPI
from task.serializers import TaskListSerializer,UserTaskCreateSerializer,UserTaskListSerializer
# Create your views here.


class TaskListAPI(AbstractListAPI):

    serializer_class = TaskListSerializer
    pagination_class = None
    queryset = TaskListSerializer.get_query()

class UserTaskCreateAPI(AbstractCreateAPI):

    serializer_class = UserTaskCreateSerializer


class UserTaskListAPI(AbstractListAPI):

    serializer_class = UserTaskListSerializer
    pagination_class = None
    

    def get_queryset(self):
        return UserTaskListSerializer.get_query(self.request.user)
     