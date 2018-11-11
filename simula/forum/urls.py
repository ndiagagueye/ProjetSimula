from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import(
     detail_post,
     add_comment,
     create_post,
     show_category,
     home,

      )
#from blog.views.register import RegisterView
app_name = 'forum'
urlpatterns = [

    
      path('post/<int:pk>/detail', detail_post, name = "detail_post"),
      path('',  home, name = "home"),
      path('add_comment', add_comment, name = "add_comment"),
      path('create/', create_post, name='create_post'),
      path('categorie/<int:pk>/', show_category, name = 'show_category'),
      

]