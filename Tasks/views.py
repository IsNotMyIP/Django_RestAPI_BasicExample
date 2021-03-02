from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import TareaSerializer
from .models import Tarea


class index(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
# Create your views here.

def u_tarea(request, task_id):
    return(HttpResponse("Una tarea :D"))

def addTarea(request):
    return(HttpResponse("Añade!!"))

def delTarea(request, task_id):
    return(HttpResponse("Pues borro la tarea"))
