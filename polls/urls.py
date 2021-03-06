
from django.conf.urls import patterns,url,include

from django.conf.urls import url
from polls.views import *

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    
    url(r'^show1/$', views.show1, name='show1'),
    url(r'^script/$', views.script, name='script'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^show2/$', views.show2, name='show2'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
   
    url(r'^email/$',views.email,name='email'),
    url(r'^thanks/$',views.thanks,name='thanks'),
]

