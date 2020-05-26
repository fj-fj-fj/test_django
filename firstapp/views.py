from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .models import Post, Tag
from .forms import PostForm, TagForm
from .utils import (ObjectDetailMixin, ObjectCreateMixin,
                    ObjectUpdateMixin, ObjectDeleteMixin)


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


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'firstapp/post_delete_form.html'
    redirect_url = 'posts_list_url'


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


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'firstapp/tag_delete_form.html'
    redirect_url = 'tags_list_url'
