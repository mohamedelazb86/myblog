from django.shortcuts import render
from .models import Post

def post_list(request):
    posts=Post.objects.all()
    context={
        'post_list':posts
    }
    return render (request,'posts/post_list.html',context)


def post_detail(request,pk):
    post=Post.objects.get(id=pk)

    context={
        'post':post
    }
    return render(request,'posts/post_detail.hml',context)


