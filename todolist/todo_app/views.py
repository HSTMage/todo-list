from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from todo_app.models import Todo, Tags
    
def index(request):
    latest_list = Todo.objects.order_by('-date_cre')[:10]
    
    context = { 'latest_list': latest_list}
    return render(request, 'todo_app/index.html', context)   
    
    
def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo_app/detail.html', {'todo': todo})