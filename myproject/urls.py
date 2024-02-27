
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("cr/", admin.site.urls),
    # path("members/", include("django.contrib.auth.urls")),  # for authentication
    path("", include("members.urls")),
]
