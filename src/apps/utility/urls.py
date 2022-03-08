from django.urls import path

from utility.views import MetaContentDetailAPI,MetaContentListAPI

urlpatterns = [
    path("meta/<str:pk>/",MetaContentDetailAPI.as_view()),
    path("meta/list/",MetaContentListAPI.as_view())
]
