from django.shortcuts import render

from todo_app.models import Todo, Tags
from activity_log.models import ActivityLog

def index(request):
    latest_list = ActivityLog.objects.order_by('-date')[:10]   
    context = { 'latest_list': latest_list} 

    return render(request, 'activity_log/index.html', context)   
