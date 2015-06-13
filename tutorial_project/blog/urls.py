from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^hello/$', 'blog.views.hello'),
    url(r'^goodbye/$', 'blog.views.good_bye'),
    url(r'^request/$', 'blog.views.request_dump'),
    url(r'^reverser/$', 'blog.views.reverser'),
    ##
    url(r'^tpl/hello/$', 'blog.views.tpl_hello'),
)
