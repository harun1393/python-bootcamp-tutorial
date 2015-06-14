from django.conf.urls import patterns, include, url
from rest_framework import routers

from .api import *


router = routers.DefaultRouter()
router.register(r'author', AuthorViewSet, base_name="author-api")
router.register(r'blog', BlogViewSet, base_name="blog-api")
router.register(r'post', PostViewSet, base_name="post-api")
router.register(r'comment', CommentViewSet, base_name="comment-api")
router.register(r'tag', TagViewSet, base_name="tag-api")


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)), ## <---------- Register the Router!
    url(r'^hello/$', 'blog.views.hello'),
    url(r'^goodbye/$', 'blog.views.good_bye'),
    url(r'^request/$', 'blog.views.request_dump'),
    url(r'^reverser/$', 'blog.views.reverser'),
    ##
    url(r'^tpl/hello/$', 'blog.views.tpl_hello'),
    ##
    url(r'^author/$', 'blog.views.author_list', name='author-list'),
    url(r'^author/create/$', 'blog.views.author_create', name='author-create'),
    url(r'^author/update/(?P<pk>[0-9]+)/$', 'blog.views.author_update', name='author-update'),
    url(r'^author/detail/(?P<pk>[0-9]+)/$', 'blog.views.author_detail', name='author-detail'),
    url(r'^author/delete/(?P<pk>[0-9]+)/$', 'blog.views.author_delete', name='author-delete'),
)
