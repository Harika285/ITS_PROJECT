
from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r"^account/", include("account.urls")),
=======

urlpatterns = [
    url(r'^polls/', include('polls.urls')),

>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9
    url(r'^admin/', admin.site.urls),
]
