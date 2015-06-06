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
    LoginForm, )

from django.utils import timezone
from .models import Campaign
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
        start_at__lte=date, end_at__gte=date).order_by('-start_at')[:6]
    return render(request, 'app_users/dashboard.html', locals())


def campaign(request):
    """
    campaign view
    """
    date = datetime.date(timezone.now())
    campaigns = Campaign.objects.filter(
        start_at__lte=date, end_at__gte=date).order_by('-start_at')
    return render(request, 'app_users/campaign.html', locals())
