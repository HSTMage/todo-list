from django.shortcuts import render

# Create your views here.

from todo_app.models import Todo, Tags
from rest_framework import viewsets
from todo_app.serializers import TodoSerializer, TagsSerializer

clas TodoListView(view.ModelView)
    queryset = Todo.objects.all()


"""
#class TodoViewSet(viewsets.ModelViewSet):
#queryset = Todo.objects.all()
#serializer_class = TodoSerializer

#class TagsViewSet(viewsets.ModelViewSet):
# queryset = Tags.objects.all()
# serializer_class = TagsSerializer
"""