from django.urls import path

from banners.views import BannerListAPI


urlpatterns = [
    path("list/",BannerListAPI.as_view())
]
