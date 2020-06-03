from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .models import Post, Tag
from .forms import PostForm, TagForm
from .utils import (ObjectDetailMixin, ObjectCreateMixin,
                    ObjectUpdateMixin, ObjectDeleteMixin)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }
    return render(request, 'firstapp/index.html', context)


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'firstapp/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'firstapp/post_create.html'
    raise_exeption = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'firstapp/post_update_form.html'
    raise_exeption = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'firstapp/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exeption = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'firstapp/tags_list.html', {'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'firstapp/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'firstapp/tag_create.html'
    raise_exeption = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'firstapp/tag_update_form.html'
    raise_exeption = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'firstapp/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exeption = True
