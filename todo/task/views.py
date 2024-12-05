from django.shortcuts import render
from frame.base_views import (
    BaseCreateView,
    BaseListView,
    BaseUpdateView,
    BaseDeleteView,
    BaseDetailView,
)
from .models import Task
from django.urls import reverse_lazy
# Create your views here.


class TaskCreateView(BaseCreateView):
    model = Task
    success_url = reverse_lazy("task-list")


class TaskListView(BaseListView):
    model = Task


class TaskUpdateView(BaseUpdateView):
    model = Task
    success_url = reverse_lazy("task-list")


class TaskDeleteView(BaseDeleteView):
    model = Task
    success_url = reverse_lazy("task-list")


class TaskDetailView(BaseDetailView):
    model = Task
