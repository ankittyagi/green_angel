__author__ = 'Tarun Behal'

from django.conf.urls import patterns, include, url
from .views import (user_login, home, app_logout,)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^login/$', user_login, name='login'),
                       url(r'^logout/$',
                           app_logout, name='logout'),
                       url(r'^$', home, name='home'),
                       ) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
