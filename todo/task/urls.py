from django.urls import path
from .views import (
    TaskCreateView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetailView,
    TagCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagDetailView,
)

urlpatterns = [
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/list/', TaskListView.as_view(), name='task-list'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tag/create/', TagCreateView.as_view(), name='tag-create'),
    path('tag/list/', TagListView.as_view(), name='tag-list'),
    path('tag/update/<int:pk>/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/delete/<int:pk>/', TagDeleteView.as_view(), name='tag-delete'),
    path('tag/detail/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]
