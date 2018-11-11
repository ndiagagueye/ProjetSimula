from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.core.mail import BadHeaderError, EmailMessage
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views import generic
from datetime import datetime
import json


def show_category(request, pk):
    posts = Post.objects.filter(category__id=pk, publish=True)
    category = get_object_or_404(Category, id=pk)
    categories = Category.objects.all().order_by('-date')
    nowtime = datetime.now()
    return render(request, "forum/show_category.html", locals())


@login_required
def home(request):
    categories = Category.objects.all().order_by('-date')
    posts = Post.objects.filter(publish=True).order_by('-date')
    comments = Comment.objects.all().order_by('date')
    form = CommentForm(request.POST)


    return render(request, "forum/home.html", locals())


@login_required
def detail_post(request, pk):
    categories = Category.objects.all().order_by('-date')
    post = Post.objects.get(id=pk)
    nowtime = datetime.now()
    comments = Comment.objects.filter(post__id=pk).order_by('date')
    form = CommentForm(request.POST)

    return render(request, "forum/detail_post.html", locals())


@login_required
def create_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/forum/detail_post')

    return render(request, "forum/create_post.html", locals())


def add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('body')
        response_data = {}
        post = Post.objects.get(id=request.POST.get('post_id'))
        date = datetime.now()
        comment = Comment(body=comment_text, user=request.user, post=post)
        comment.save()

        response_data['result'] = 'Create post successful!'
        response_data['commentid'] = comment.id
        response_data['body'] = comment.body
        response_data['user'] = comment.user.username
        response_data['id'] = comment.post.id

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
