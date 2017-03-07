<<<<<<< HEAD
from django.conf.urls import url,include
=======
from django.conf.urls import url
>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9

from . import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    # ex: /polls/
<<<<<<< HEAD
    url(r'^show1/$', views.show1, name='show1'),
    url(r'^show2/$', views.show2, name='show2'),
    #url(r'^show/$', views.show, name='show'),

    # ex: /polls/5/
    #url(r"^account/signup/$", views.SignupView.as_view(), name="account_signup"),
    #url(r"^account/", include("account.urls")),
=======
    #url(r'^(?[a-z]+).html/$', views.show, name='show'),
    # ex: /polls/5/
>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

