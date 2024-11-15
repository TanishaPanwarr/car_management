from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views

# Setting up Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Car Management API",
      default_version='v1',
      description="API documentation for Car Management Application",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),  # Include car app URLs
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api_docs'),  # Swagger documentation

    path('api/auth/', include('rest_auth.urls')),  # for login/logout
    path('api/auth/registration/', include('rest_auth.registration.urls')),  # for signup
]




