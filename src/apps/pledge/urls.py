from django.urls import path

from pledge.views import PledgeListAPI,PledgeDetailAPI,UserPledgeCreateAPI,UserPledgeRetrieveAPI

urlpatterns = [
    path("list/",PledgeListAPI.as_view()),
    path("detail/<int:pk>/",PledgeDetailAPI.as_view()),
    path("create/",UserPledgeCreateAPI.as_view()),
    path("retrieve/",UserPledgeRetrieveAPI.as_view()),

]
