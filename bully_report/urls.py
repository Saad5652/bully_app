
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/entities/', include('entities.urls')),

    path('admin/', admin.site.urls), 
]
