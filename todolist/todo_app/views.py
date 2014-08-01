from django.shortcuts import render

# Create your views here.

from todo_app.models import Todo, Tags
from rest_framework import viewsets
from todo_app.serializers import TodoSerializer, TagsSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TagsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer