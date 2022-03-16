from django.urls import path

from task.views import TaskListAPI,UserTaskListAPI,UserTaskCreateAPI,UserTaskStatusAPI

urlpatterns = [
    path("list/",TaskListAPI.as_view()),
    path("user/list/",UserTaskListAPI.as_view()),
    path("user/create/",UserTaskCreateAPI.as_view()),
    path("user/status/<int:pk>/",UserTaskStatusAPI.as_view())
]
