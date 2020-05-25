from django.shortcuts import render
from django.shortcuts import redirect
# from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .forms import PostForm, TagForm
from .utils import ObjectDetailMixin, ObjectCreateMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'firstapp/index.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'firstapp/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'firstapp/post_create.html'


class PostUpdate(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=post)
        return render(request, 'firstapp/post_update_form.html', {'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'firstapp/post_update.html', {'form': bound_form, 'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'firstapp/tags_list.html', {'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'firstapp/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'firstapp/tag_create.html'


class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'firstapp/tag_update_form.html', {'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'firstapp/tag_update.html', {'form': bound_form, 'tag': tag})
