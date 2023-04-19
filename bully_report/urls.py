
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('entities.urls')),
    path('api/v1/', include('reports.urls')),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
