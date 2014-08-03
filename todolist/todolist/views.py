from django.http import HttpResponse

def index(request):
    return HttpResponse("Ahojte :) Ste na stranke Todo List")