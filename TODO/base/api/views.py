from django.shortcuts import render,redirect,HttpResponse
from base.models import Todo

from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def apiview(request):
    api_urls = {
        'setup_status' : 'below API is not setup ',
        'list' : '/task-list/',
        'Detail view' : '/task-list/<int:pk>/',
        'create' : '/create/',
        'update' : '/update/<int:pk>/',
        'delete' : '/delete/<int:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    task = Todo.objects.all()
    serializer= TodoSerializer(task,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT', 'PATCH','GET'])
def update(request,pk):
    task = Todo.objects.get(id=pk)
    if request.method == "GET":
        serializer = TodoSerializer(instance=task)
    else:
        serializer = TodoSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


@api_view(['DELETE','GET'])
def delete(request,pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=task)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response("Deleted!!!")
    else:
        return Response("No match - Delete is incomplete")