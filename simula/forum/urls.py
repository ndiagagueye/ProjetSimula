from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import(
     detail_post,
     add_comment,
     create_post,
     show_category,
     home,
     update_post,
     change_post_update,
     validate_comment,

      )
#from blog.views.register import RegisterView
app_name = 'forum'
urlpatterns = [

    
      path('post/<int:pk>/detail', detail_post, name = "detail_post"),
      re_path('post/<int:pk>/detail', detail_post, name="detail_post"),

      path('',  home, name = "home"),
      path('validate_comment', validate_comment, name="validate_comment"),
      path('add_comment', add_comment, name = "add_comment"),
      path('change_post_update', change_post_update, name="change_post_update"),
      path('update_post', update_post, name = "update_post"),
      path('create/', create_post, name='create_post'),
      path('categorie/<int:pk>/', show_category, name = 'show_category'),


]