from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render

from todo_app.models import Todo, Tags
from activity_log.models import ActivityLog
from django.contrib.auth.models import User
from django.utils import timezone
    
def index(request):
    actionLog_div = render(request, 'activity_log/index.html', {}) 
    
    latest_list = Todo.objects.order_by('-date_cre')[:10]
    context = { 'latest_list': latest_list, actionLog_div: actionLog_div}
    return render(request, 'todo_app/index.html', context)   
        
def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo_app/detail.html', {'todo': todo, 'tags': todo.tags.all()})

def add(request):
    return render(request, 'todo_app/add.html', {})

def save(request):
    todo_text = request.POST['todo_text']
    todo = Todo(todo=todo_text, date_cre=timezone.now(), author=request.user)
    todo.save()
    
    user = request.user
    action = 'pridanie noveho Todo'
    
    al = ActivityLog(action=action, date=timezone.now(), author=user)
    al.save()
    
    return HttpResponseRedirect(reverse('todo:index', args=()))