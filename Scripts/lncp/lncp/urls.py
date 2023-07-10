from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lncp_members.urls')),
    path('admin/', admin.site.urls),
]
