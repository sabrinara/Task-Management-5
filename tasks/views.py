from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save() 
            return redirect('add_task') 
    else: 
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form' : task_form})

def edit_task(request, id):
    tasks = models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=tasks)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=tasks)
        if task_form.is_valid():
            task_form.save() 
            return redirect('homepage') 
        
    return render(request, 'add_task.html', {'form' : task_form})

def delete_task(request, id):
    tasks = models.Task.objects.get(pk=id)
    tasks.delete()
    return redirect('homepage')