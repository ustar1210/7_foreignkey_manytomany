from django.contrib import admin
from django.urls import path, include
from account import urls
from post import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('post.urls')),
    path("account/", include('account.urls')),
]
