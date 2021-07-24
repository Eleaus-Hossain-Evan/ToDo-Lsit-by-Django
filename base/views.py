from base.models import Task
from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'