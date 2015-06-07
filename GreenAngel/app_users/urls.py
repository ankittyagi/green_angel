__author__ = 'Tarun Behal'

from django.conf.urls import patterns, include, url
from .views import (user_login, home, app_logout, dashboard, campaign,
                    campaign_join, mycampaign, add_plantation, myplantation,
                    mypoints, redeem)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^login/$', user_login, name='login'),
                       url(r'^dashboard/$', dashboard, name='dashboard'),
                       url(r'^campaign/$', campaign, name='campaign'),
                       url(r'^mycampaign/$', mycampaign, name='mycampaign'),
                       url(r'^myplantation/$', myplantation, name='myplantation'),
                       url(r'^mypoints/$', mypoints, name='mypoints'),
                       url(r'^redeem/$', redeem, name='redeem'),
                       url(r'^logout/$',
                           app_logout, name='logout'),
                       url(r'^campaign/(?P<campaignid>\d+)/join$',
                           campaign_join, name='campaign_join'),
                       url(r'^zone/(?P<zoneid>\d+)/add$',
                           add_plantation, name='add_plantation'),
                       url(r'^$', home, name='home'),
                       ) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
