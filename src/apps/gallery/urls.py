from django.urls import path

from gallery.views import GalleryListAPI


urlpatterns = [
    path("list/",GalleryListAPI.as_view())
]
