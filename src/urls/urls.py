from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
import debug_toolbar
from .api_urls import urlpatterns as ApiUrl


schema_view = get_schema_view(
   openapi.Info(
      title="ESF API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('advanced_filters/', include('advanced_filters.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += ApiUrl



admin.site.site_header = "EFS Admin"
admin.site.site_title = "EFS Admin Portal"
admin.site.index_title = "Welcome to EFS Portal"