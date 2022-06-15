from django.urls import  path

from account.views import FCMDeviceViewAPI,RegisterViewAPI
from apps.account.views import FCMDeviceViewAPI, RegisterViewAPI,NewRegisterViewAPI,GoogleSignInAPI

urlpatterns = [
    path("register/",RegisterViewAPI.as_view(),),
    path("fcm/",FCMDeviceViewAPI.as_view(),),
    path("new/",NewRegisterViewAPI.as_view()),
    path("google/<str:pk>/",GoogleSignInAPI.as_view())
]
