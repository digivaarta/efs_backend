from django.urls import  path
from profiles.views import UserProfileAPI

urlpatterns = [
    path("profile/",UserProfileAPI.as_view())
]
