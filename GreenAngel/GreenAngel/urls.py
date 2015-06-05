from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'GreenAngel.views.home', name='home'),
                       url(r'^', include('app_users.urls')),
                       url('', include(
                           'social.apps.django_app.urls', namespace='social')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
