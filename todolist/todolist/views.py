from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):    
    user = request.user
    is_on = user.is_authenticated() 

    context = { 'user' : user, 'is_on' : is_on}  
    return render(request, 'todolist/index.html', context)
    
def doLogin(request):
    username = request.POST['login_name']
    password = request.POST['login_pass']
    
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        err_message = 'invalid login'
        
    return HttpResponseRedirect(reverse('index', args=()))  
    
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
        is_ok1 = True
    else:
        is_ok1 = False
        
    if password == password2:
        is_ok2 = True
    else: 
        is_ok2 = False
        
    if is_ok1 & is_ok2:
        new_user = User.objects.create_user(username, '', password)
        new_user.save()
    else:
        err_msg = 'Pouzivatelske meno sa pouziva alebo boli zle zadane hesla'

    return HttpResponseRedirect(reverse('index', args=())) 