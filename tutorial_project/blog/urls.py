from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
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
