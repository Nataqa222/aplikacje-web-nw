from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.api_urls')),  # API REST
    path('myapp/', include('myapp.urls')),    # Widoki HTML
]
