from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from activity_log.models import ActivityLog
from django.utils import timezone

def index(request):    
    user = request.user
    is_on = user.is_authenticated() 
 
    if is_on:
        return HttpResponseRedirect(reverse('todo:index', args=()))     
    else:
        context = { 'user' : user }  
        return render(request, 'todolist/index.html', context)
                                                                     
def doLogin(request):
    username = request.POST['login_name']
    password = request.POST['login_pass']
    
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        
        al = ActivityLog(action='uspesne prihlasenie',date=timezone.now(), author=user)
        al.save()
        return HttpResponseRedirect(reverse('index', args=()))  
    else:
        err_message = 'nespravne prihlasenie' 
        return render(request, 'todolist/index.html', {'err_msg': err_message})       
    
    
def doLogout(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('index', args=())) 
    
def register(request):
    return render(request, 'todolist/register.html', {})
    
def doRegister(request):
    username  = request.POST['reg_name']
    password  = request.POST['reg_pass']
    password2 = request.POST['reg_pass2']
    
    if User.objects.filter(username=username).exists():
        is_ok1 = False
    else:
        is_ok1 = True
        
    if password == password2:
        is_ok2 = True
    else:
        is_ok2 = False
    
    if is_ok1 and is_ok2:
        new_user = User.objects.create_user(username, '')
        new_user.set_password(password)
        new_user.save()
        
        return HttpResponseRedirect(reverse('index', args=()))
    else:             
        err_msg = 'Pouzivatelske meno sa pouziva alebo boli zle zadane hesla'
        
        return render(request, 'todolist/register.html', {'err_msg': err_msg})
             