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
from django.db.models import Sum
from django.utils import timezone
from .models import Campaign, CampaignZone, Plantation
from datetime import datetime
import json
import imghdr
from django.views.decorators.csrf import csrf_exempt


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


@login_required
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
    ppts = Plantation.objects.filter(
        user=request.user, status='draft'
    ).aggregate(Sum('points'))['points__sum'] or 0
    apts = Plantation.objects.filter(
        user=request.user, status='approve'
    ).aggregate(Sum('points'))['points__sum'] or 0
    tlen = Plantation.objects.filter(
        user=request.user
    ).count()
    notmsg = 'Hi {0}, welcome to Green Angel.'.format(request.user.username)
    return render(request, 'app_users/dashboard.html', locals())


@login_required
def campaign(request):
    """
    campaign view
    """
    date = datetime.date(timezone.now())
    campaigns = Campaign.objects.filter(
        start_at__lte=date, end_at__gte=date).order_by('-id')
    return render(request, 'app_users/campaign.html', locals())


@login_required
def mycampaign(request):
    """
    mycampaign view
    """
    zones = request.user.profile.zones.all().order_by('-id')
    return render(request, 'app_users/mycampaign.html', locals())


@login_required
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
            return HttpResponseRedirect('/mycampaign')
    ex_zone = request.user.profile.zones.all()
    form.fields['zone'].queryset = CampaignZone.objects.filter(
        campaign=campaign).exclude(id__in=ex_zone)
    return render(request, 'app_users/addzone.html', locals())


@login_required
@csrf_exempt
def add_plantation(request, zoneid):
    """
    AddPlantationForm view
    """
    zone = get_object_or_404(CampaignZone, id=zoneid)
    form = AddPlantationForm()
    if request.method == 'POST':
        newpic = request.FILES.get('doc', None)
        res = {'success': False}
        if Plantation.objects.filter(user=request.user,
                                     zone=zone).count() >= 10:
            res['message'] = 'Maximum 10 trees allowed per zone.!'
            return HttpResponse(json.dumps(res),
                                content_type='application/json')
        if newpic:
            try:
                ftype = imghdr.what(newpic)
                if ftype:
                    point = int(
                        float(zone.total_points) / float(zone.total_plants))
                    Plantation.objects.create(user=request.user,
                                              zone=zone,
                                              photo=newpic,
                                              points=point)
                    res['success'] = True
                else:
                    res['message'] = "Please select image file.!"
            except Exception, e:
                res['error'] = False
                res['message'] = str(e)
        return HttpResponse(json.dumps(res), content_type='application/json')
    return render(request, 'app_users/addplantation.html', locals())


@login_required
def myplantation(request):
    """
    myplantation view
    """
    mps = Plantation.objects.filter(user=request.user).order_by('-id')
    return render(request, 'app_users/myplantation.html', locals())


@login_required
def mypoints(request):
    """
    myplantation view
    """
    pts = Plantation.objects.filter(user=request.user).order_by('-id')
    ppts = Plantation.objects.filter(
        user=request.user, status='draft'
    ).aggregate(Sum('points'))['points__sum'] or 0
    apts = Plantation.objects.filter(
        user=request.user, status='approve'
    ).aggregate(Sum('points'))['points__sum'] or 0
    return render(request, 'app_users/mypoints.html', locals())


@login_required
def redeem(request):
    """
    redeem view
    """
    apts = Plantation.objects.filter(
        user=request.user, status='approve'
    ).aggregate(Sum('points'))['points__sum'] or 0
    return render(request, 'app_users/redeem.html', locals())
