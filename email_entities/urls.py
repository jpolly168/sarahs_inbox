from django.views.generic.simple import direct_to_template, redirect_to
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^label/(?P<thread_industry>[\w\-]+)/', 'mail.views.threads_by_industry', name='thread_by_industry'),       
)