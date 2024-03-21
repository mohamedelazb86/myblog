from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class Post_List(ListView):
    model=Post
    template_name='posts/post_list.html'

class Post_Detail(DetailView):
    model=Post
    template_name='posts/post_detail.html'

class Update_Post(UpdateView):
    model=Post
    fields='__all__'
    template_name='posts/update_post.html'
    success_url='/posts/'

class Create_Post(CreateView):
    model=Post
    fields='__all__'
    template_name='posts/create_post.html'
    success_url='/posts/'

class Delete(DeleteView):
    model=Post
    template_name='posts/delete_post.html'
    success_url='/posts/'
    
    




