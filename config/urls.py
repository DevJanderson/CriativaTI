"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("reload/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', include('appSite.urls'))
]
