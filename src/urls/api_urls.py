from django.contrib import admin
from django.urls import path,include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from account import urls as authUrls
from banners import urls as bannerUrls
from gallery import urls as galleryUrls
from news import urls as newsUrls
from task import urls as taskUrls

schema_view = get_schema_view(
   openapi.Info(
      title="ESFS API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

apiDocUrls = [
    path('swaggerdocs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('apidocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    

]

urlpatterns = [
   path("authentication/",include(authUrls)),
   path("banner/",include(bannerUrls)),
   path("gallery/",include(galleryUrls)),
   path("news/", include(newsUrls)),
   path("task/", include(taskUrls)),
   path('auth/', include('dj_rest_auth.urls')),
   path('dj-rest-auth/', include('dj_rest_auth.urls')),
]


urlpatterns += [

] + apiDocUrls