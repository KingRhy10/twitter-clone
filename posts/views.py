from ast import Return
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect("form.erros.as_json()")

    # Get all posts, limit = 140
    posts = Post.objects.all()[:1400]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def like(request, post_id):
    like = Post.objects.get(id=post_id)
    like.like += 1
    like.save()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'GET':
        posts = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {'posts': posts})
    if request.method == 'POST':
        epost = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=epost)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('not valid')
