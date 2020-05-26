from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .forms import PostForm, TagForm
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'firstapp/index.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'firstapp/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'firstapp/post_create.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'firstapp/post_update_form.html'


class PostDelete(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'firstapp/post_delete_form.html', {'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'firstapp/tags_list.html', {'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'firstapp/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'firstapp/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'firstapp/tag_update_form.html'


class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'firstapp/tag_delete_form.html', {'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))
