from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save() 
            return redirect('add_category') 
    else: 
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_form})

def edit_category(request, id):
    categories = models.Category.objects.all(pk=id)
    category_form = forms.CategoryForm(instance=categories)
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST, instance=categories)
        if category_form.is_valid():
            category_form.save() 
            return redirect('home') 
    else:
        category_form = forms.CategoryForm(instance=categories)
    return render(request, 'add_category.html', {'form' : category_form})