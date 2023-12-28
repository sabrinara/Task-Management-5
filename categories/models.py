from django.db import models
from tasks.models import Task
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.name