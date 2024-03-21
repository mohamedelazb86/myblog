from django.urls import path
from .views import post_detail,post_list,create_post,update_post,delete
from .view2 import Post_List,Post_Detail,Update_Post,Create_Post,Delete


urlpatterns = [
    path('',post_list),
    path('<int:pk>/detail',post_detail),
    path('create_post',create_post),
    path('<int:pk>/update',update_post),
    path('<int:pk>/delete',delete),

    # url CBV
    path('posts/cbv',Post_List.as_view()),
    path('cbv/<int:pk>/detail',Post_Detail.as_view()),
    path('cbv/update/<int:pk>',Update_Post.as_view()),
    path('cbv/create',Create_Post.as_view()),
    path('cbv/delete/<int:pk>',Delete.as_view()),
]
