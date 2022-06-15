from django.urls import  path
from profiles.views import UserProfileAPI,UserOtpAPI

urlpatterns = [
    path("profile/",UserProfileAPI.as_view()),
    path("otp/",UserOtpAPI.as_view())
]
