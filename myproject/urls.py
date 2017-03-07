
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r"^account/", include("account.urls")),
    url(r'^admin/', admin.site.urls),
]
