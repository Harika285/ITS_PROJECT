
from django.conf.urls import patterns,url,include

from django.conf.urls import url
from polls.views import *

from . import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^show1/$', views.show1, name='show1'),
     url(r'^home/$', views.page, name='home'),
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

]

