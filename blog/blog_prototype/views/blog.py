from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from blog_prototype.inputs.blog import (
    CommentCreateInput,
    CommentUpdateInpute,
    PostCreateInput,
    PostUpdateInpute,
)
from blog_prototype.services.blog import CommentService, PostService


@login_required
def post_list(request):

    post_service = PostService()
    posts = post_service.list_post()

    context = {
        'posts': posts,
    }

    return render(request, 'blog_prototype/blog/post_list.html', context)


@login_required
def post_create(request):

    user_id = request.user.id

    if request.method == 'POST':
        data = request.POST.dict()
        data['user_id'] = user_id
        post_service = PostService()
        input_data = PostCreateInput(**data)
        post_service.create_post(input_data)
        return redirect('post-list')

    return render(request, 'blog_prototype/blog/post_create.html')


@login_required
def post_view(request, post_id):

    user_id = request.user.id

    post_service = PostService()
    post = post_service.get_post(post_id)

    if request.method == 'POST':
        data = request.POST.dict()
        data['user_id'] = user_id
        data['post_id'] = post_id
        comment_service = CommentService()
        input_data = CommentCreateInput(**data)
        comment_service.create_comment(input_data)

        return redirect('post-view', post_id=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog_prototype/blog/post_view.html', context)
