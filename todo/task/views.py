from django.shortcuts import render
from frame.base_views import (
    BaseCreateView,
    BaseListView,
    BaseUpdateView,
    BaseDeleteView,
    BaseDetailView,
)
from .models import Task, Tag
from django.urls import reverse_lazy
# Create your views here.

class TaskCreateView(BaseCreateView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskListView(BaseListView):
    model = Task

class TaskUpdateView(BaseUpdateView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskDeleteView(BaseDeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskDetailView(BaseDetailView):
    model = Task

class TagCreateView(BaseCreateView):
    model = Tag
    success_url = reverse_lazy('tag-list')

class TagListView(BaseListView):
    model = Tag

class TagUpdateView(BaseUpdateView):
    model = Tag
    success_url = reverse_lazy('tag-list')

class TagDeleteView(BaseDeleteView):
    model = Tag
    success_url = reverse_lazy('tag-list')

class TagDetailView(BaseDetailView):
    model = Tag

