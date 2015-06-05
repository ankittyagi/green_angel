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


def user_login(request):
    """
    login view
    """
    form = LoginForm()
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
                    return HttpResponse('login sucees')
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
    return HttpResponse('this is home')
