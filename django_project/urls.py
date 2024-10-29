from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("api/rooms", include("pages.urls")),
    path("api/messages", include("pages.urls")),
]
