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
from django.utils.safestring import mark_safe
from django.db.models import Q
from django import template

register = template.Library()

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
    is_superuser = False


    room_name_json = 'post-'+mark_safe(json.dumps(pk))
    if request.user.is_superuser:
        is_superuser = True

    return render(request, "forum/detail_post.html", locals())


@login_required
def create_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/forum')

    return render(request, "forum/create_post.html", locals())

@login_required()
def add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('body')
        response_data = {}
        post = Post.objects.get(id=request.POST.get('post_id'))
        date = datetime.now()
        comment = Comment(body=comment_text, user=request.user, post=post)
        comment.save()
        post.update = True
        post.save()
        response_data['result'] = 'Create post successful!'
        response_data['commentid'] = comment.id
        response_data['body'] = comment.body
        response_data['user'] = comment.user.username
        response_data['post_id'] = comment.post.id

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def update_post(request):
    post_id = request.POST['id']
    post = Post.objects.get(id=post_id)
    response_data = {'update': post.update}
    if post.update:
        comment = Comment.objects.filter(post__id=post_id).last()
        response_data['comment_id'] = comment.id
        response_data['comment_body'] = comment.body
        response_data['comment_username'] = comment.user.username
    return HttpResponse(
        json.dumps(response_data),
        content_type='application/json')


def change_post_update(request):
    post_id = request.POST['id']
    post = Post.objects.get(id=post_id)
    post.update = False
    post.save()
    response_data = {'update': 'Succes'}
    return HttpResponse(
        json.dumps(response_data),
        content_type='application/json')

@login_required()
def validate_comment(request):
    comment_id = request.POST['comment_id']
    comment_validate = Comment.objects.get(id=comment_id)
    comment_validate.validate = True
    comment_validate.save()
    return HttpResponse(
        json.dumps(True),
        content_type='application/json')

























































# @register.filter
# def time_ago(timestamp=None):
#
#     timeDiff = datetime.datetime.now() - timestamp
#     days = timeDiff.days
#     hours = timeDiff.seconds / 3600
#     minutes = timeDiff.seconds % 3600 / 60
#     seconds = timeDiff.seconds % 3600 % 60
#
#     str = ""
#     tStr = ""
#     if days > 0:
#         if days == 1:
#             tStr = "jour"
#         else:
#             tStr = "jours"
#         str = str + "%s %s" % (days, tStr)
#         return str
#     elif hours > 0:
#         if hours == 1:
#             tStr = "heure"
#         else:
#             tStr = "heures"
#         str = str + "%s %s" % (hours, tStr)
#         return str
#     elif minutes > 0:
#         if minutes == 1:
#             tStr = "minute"
#         else:
#             tStr = "minutes"
#         str = str + "%s %s" % (minutes, tStr)
#         return str
#     elif seconds > 0:
#         if seconds == 1:
#             tStr = "seconde"
#         else:
#             tStr = "secondes"
#         str = str + "%s %s" % (seconds, tStr)
#         return str
#     else:
#         return None