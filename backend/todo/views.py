from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class TodoView(viewsets.ModelViewSet):

    @method_decorator(csrf_exempt)
    def dispathch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
