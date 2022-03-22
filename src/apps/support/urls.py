from django.urls import path

from support.views import TicketCreateAPI,SupportCreateAPI,TicketListAPI,SupportListAPI,TicketUpdateAPI

urlpatterns = [
    path("ticket/create/",TicketCreateAPI.as_view()),
    path("ticket/update/<int:pk>/",TicketUpdateAPI.as_view()),
    path("support/create/",SupportCreateAPI.as_view()),
    path("ticket/list/",TicketListAPI.as_view()),
    path("support/list/",SupportListAPI.as_view()),

]
