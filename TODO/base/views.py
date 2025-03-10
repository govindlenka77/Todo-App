from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'base/home.html', context)

def start(request):
    return HttpResponse("Hiii")

def update(request,pk):
    task = Todo.objects.get(id= pk)
    form = TodoForm(instance=task)
    # task_time = task.date_time
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'pk' : pk, 'form' : form}
    return render(request, 'base/update.html',context)

def delete(request, pk):
    task = Todo.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    context = {'pk' : pk, 'task' : task}
    return render(request,'base/delete.html', context)