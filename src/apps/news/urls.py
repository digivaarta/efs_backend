from django.urls import path

from news.views import NewsListAPI


urlpatterns = [
    path("list/",NewsListAPI.as_view())
]
