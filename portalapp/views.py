from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from portalapp.models import *
from portalapp.forms import getUserInfo
from django.shortcuts import get_object_or_404
import re
from django.views.generic.edit import UpdateView
from django.db.models import Q
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.db import transaction

def index(request):
    if request.user.is_authenticated:
        if request.user.role == 'Alumni':
            return redirect('aluminDashboard')
    return render(request,"main/landing.html",{'user':None})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import alumniUser

def customLogin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            username1 = request.POST.get('logusername')
            password1 = request.POST.get('logpassword')
            user = authenticate(request=request, username=username1, password=password1)
            print(user,username1,password1)
            if user is not None:
                login(request, user)
                if user.role == 'Alumni':
                    return redirect('aluminDashboard')
                return redirect('/')
            else:
                return HttpResponse("Invalid credentials")
        
        elif action == 'signup':
            username = request.POST.get('username')
            password = request.POST.get('password')
            roll_no = request.POST.get('roll_no')
            phone = request.POST.get('phone')
            role = 'Alumni' if request.POST.get('is_alumin') else 'Student'
            print(role)
            user = alumniUser.objects.create_user(username=username)
            user.set_password(password)
            user.roll_no = roll_no
            user.phone_no = phone
            user.role = role
            user.save()

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                if request.user.role == 'Alumni':
                    return redirect('aluminDashboard')
                return redirect('/')

    return render(request, 'main/home/login/login.html')

def alumniHome(request):
    return render(request, 'main/home/index.html')

def customLogout(request):
    logout(request)
    return redirect('/')

def alumniEvents(request):
    event = events.objects.all()
    return render(request, 'main/events/event.html')


def alumniSuccess(request):
    stories = successtory.objects.all()
    if request.method == 'POST':
        story = request.POST.get('story')
        ss = successtory.objects.create(alumni = request.user,story=story)
        ss.save()
    return render(request, 'main/success/s.html',{'stories':stories})

def alumniInnovations(request):
    return render(request, 'main/innovation/inno.html')

def createQuery(request):
    queri = queries.objects.all()
    if request.method == 'POST':
        query = request.POST.get('query')
        topic = request.POST.get('topic')
        quer = queries.objects.create(alumni = request.user,topic = topic,query=query)
        quer.save()
        return render(request, 'main\student\index.html',{'allquery':queri})
    return render(request, 'main\student\index.html',{'allquery':queri})

def alumniDashboard(request):
    return render(request, 'main\home\\alumni.html')

def donations(request):
    return render(request, 'main\home\donations\do.html')

def workshop(request):
    return render(request, 'main\workshop\workshop.html')

def addEvent(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        event_title = request.POST.get('event_title')
        event_date = request.POST.get('event_date')
        event_location = request.POST.get('event_location')
        event_description = request.POST.get('event_description')
        event = events.objects.create(alumni=request.user, event=event,title=event_title, date=event_date, location=event_location, desc=event_description)
        event.save()
        return redirect('alumniDashboard')
    return render(request, 'main\home\workshop\\addEvents.html')
