from asyncio import Task
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Tasks

# Create your views here.


def home(request):

    tasks = Tasks.objects.all()

    context = {
        'tasks':tasks
    }


    return render(request,'home.html',context)
def create_task(request):

    if request.method == 'POST':

        task = request.POST['task']

        task = Tasks.objects.create(name = task)
        task.save()


    return redirect('home')


def mark_task(request,pk):

    task = Tasks.objects.get(id=pk)
    task.is_active = True
    task.save()
    return redirect('home')


def delete_task(request,pk):

    task = Tasks.objects.get(id = pk)
    task.delete()
    return redirect('home')

    