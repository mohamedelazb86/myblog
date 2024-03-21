from django.urls import path
from .views import post_detail,post_list


urlpatterns = [
    path('',post_list),
    path('<int:pk>/detail',post_detail),
]
