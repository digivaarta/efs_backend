from django.urls import path

from scholarship.views import ScholarshipListAPI,UserScholarshipTaskCreateAPI,UserScholarshipTaskListAPI,UserScholarshipTaskVerifyAPI

urlpatterns = [
    path("list/",ScholarshipListAPI.as_view()),
    # path("detail/<int:pk>/",PledgeDetailAPI.as_view()),
    path("create/",UserScholarshipTaskCreateAPI.as_view()),
    path("user/list/",UserScholarshipTaskListAPI.as_view()),
    path("user/verify/",UserScholarshipTaskVerifyAPI.as_view()),
    # path("retrieve/",UserPledgeRetrieveAPI.as_view()),

]
