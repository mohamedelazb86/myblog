from django.urls import path
from .views import post_detail,post_list,create_post,update_post


urlpatterns = [
    path('',post_list),
    path('<int:pk>/detail',post_detail),
    path('create_post',create_post),
    path('<int:pk>/update',update_post),
]
