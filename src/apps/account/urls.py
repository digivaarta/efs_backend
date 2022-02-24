from django.urls import  path

from account.views import FCMDeviceViewAPI,RegisterViewAPI
from apps.account.views import FCMDeviceViewAPI, RegisterViewAPI

urlpatterns = [
    path("register/",RegisterViewAPI.as_view(),),
    path("fcm/",FCMDeviceViewAPI.as_view(),)
]
