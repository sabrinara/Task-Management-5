from django import forms
from tasks.models import Task
# from categories.models import Category

class TaskForm(forms.ModelForm):
    # category = forms.ModelMultipleChoiceField( queryset=Category.objects.all(),  widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Task
        fields = '__all__'
       