from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'firstapp/index.html', {'posts': posts})


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'firstapp/post_detail.html', {'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'firstapp/tags_list.html', {'tags': tags})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'firstapp/tag_detail.html', {'tag': tag})
