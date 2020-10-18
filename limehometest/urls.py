from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from limehometest import settings

schema_view = get_schema_view(
    openapi.Info(
        title="LimeHomeTest API",
        default_version='v0.1',
        description="Docs on LimeHomeTest Api.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('bookings/', include('bookings.urls', namespace='bookings'), ),
    path('properties/', include('properties.urls', namespace='properties'), ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
