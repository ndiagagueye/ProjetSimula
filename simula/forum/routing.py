
# chat/routing.py
from django.conf.urls import url, re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/post/(?P<id_post>[^/]+)/$', consumers.CommentConsumer),
]
