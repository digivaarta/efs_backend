from django.urls import path

from utility.views import MetaContentDetailAPI

urlpatterns = [
    path("meta/<str:pk>/",MetaContentDetailAPI.as_view())
]
