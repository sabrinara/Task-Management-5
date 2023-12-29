from django.shortcuts import render
from tasks.models import Task
# from categories.models import Category

def home (request):
    tasks = Task.objects.all()
    # tasks = Category.objects.all()

    return render(request, 'index.html', {'tasks' : tasks})