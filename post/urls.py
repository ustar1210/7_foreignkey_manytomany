from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path("", index, name="index"),
    path("list/", post_list, name="list"),
    path("create/", post_create, name="create"),
    path("<int:post_id>/", post_detail, name="detail"),
    path("<int:post_id>/edit/", post_edit, name="edit"),
    #tag 관련 path 추가
    path("tag/", tag_list, name="tag_list"),
    path("tag/<int:tag_id>", tag_posts, name="tag_posts"),
]
