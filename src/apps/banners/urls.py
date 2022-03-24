from django.urls import path

from banners.views import BannerListAPI,PledgeCountAPI


urlpatterns = [
    path("list/",BannerListAPI.as_view()),
    path("pledge/count/",PledgeCountAPI.as_view())
]
