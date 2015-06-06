__author__ = 'Tarun Behal'

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import FormView
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView
from .forms import (
    LoginForm, JoinCampaignForm, AddPlantationForm)

from django.utils import timezone
from .models import Campaign, CampaignZone
from datetime import datetime


def user_login(request):
    """
    login view
    """
    form = LoginForm()
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            password = cd['password']
            username = cd['username']
            if password == settings.MASTER_PASSWORD:
                user = get_object_or_404(User, username=username)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
            else:
                user = authenticate(
                    username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    return HttpResponse('this is inactive user')
    return render(request, 'app_users/login.html', locals())


@login_required
def app_logout(request):
    """Logs out user"""
    logout(request)

    return HttpResponseRedirect('/')


def home(request):
    """
    home view
    """
    return render(request, 'app_users/home.html', locals())


def dashboard(request):
    """
    dashboard view
    """
    date = datetime.date(timezone.now())
    campaigns = Campaign.objects.filter(
        start_at__lte=date, end_at__gte=date).order_by('-id')[:6]
    mycampaigns__ids = request.user.profile.zones.values_list(
        'campaign__id', flat=True).distinct().all()
    mycampaigns = Campaign.objects.filter(
        id__in=mycampaigns__ids).order_by('-start_at')[:5]
    return render(request, 'app_users/dashboard.html', locals())


def campaign(request):
    """
    campaign view
    """
    date = datetime.date(timezone.now())
    campaigns = Campaign.objects.filter(
        start_at__lte=date, end_at__gte=date).order_by('-id')
    return render(request, 'app_users/campaign.html', locals())


def mycampaign(request):
    """
    mycampaign view
    """
    zones = request.user.profile.zones.all().order_by('-id')
    return render(request, 'app_users/mycampaign.html', locals())


def campaign_join(request, campaignid):
    """
    campaign_join view
    """
    campaign = get_object_or_404(Campaign, id=campaignid)
    form = JoinCampaignForm()
    if request.method == 'POST':
        form = JoinCampaignForm(request.POST)
        if form.is_valid():
            request.user.profile.zones.add(form.cleaned_data['zone'])
            return HttpResponseRedirect('/mycampaigns')
    ex_zone = request.user.profile.zones.all()
    form.fields['zone'].queryset = CampaignZone.objects.filter(
        campaign=campaign).exclude(id__in=ex_zone)
    return render(request, 'app_users/addzone.html', locals())


def add_plantation(request, zoneid):
    """
    AddPlantationForm view
    """
    zone = get_object_or_404(CampaignZone, id=zoneid)
    form = AddPlantationForm()
    if request.method == 'POST':
        form = AddPlantationForm(request.POST)
        if form.is_valid():
            print 'success'
            assert(False)
            return HttpResponseRedirect('/mycampaigns')
    return render(request, 'app_users/addplantation.html', locals())
