from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insurance/', include('insurance_data.urls')), 
    path('api/', include('insurance_data.urls')),
]
