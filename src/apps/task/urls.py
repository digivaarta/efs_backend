from django.urls import path

from task.views import TaskListAPI,UserTaskListAPI,UserTaskCreateAPI

urlpatterns = [
    path("list/",TaskListAPI.as_view()),
    path("user/list/",UserTaskListAPI.as_view()),
    path("user/create/",UserTaskCreateAPI.as_view())
]
