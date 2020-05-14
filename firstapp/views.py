from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'firstapp/index.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'firstapp/post_detail.html', {'post': post})
