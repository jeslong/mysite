from django.conf.urls import patterns, include, url

__author__ = 'jesselong'

urlpatterns = patterns(
    'blog.views',
    (r"", "main"),
)