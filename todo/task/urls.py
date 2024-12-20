from django.urls import path
from .views import (
    TaskCreateView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListCreateView,
    TaskListListView,
    TaskListUpdateView,
    TaskListDeleteView,
)

urlpatterns = [
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/list/", TaskListView.as_view(), name="task-list"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/detail/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task-list/create/", TaskListCreateView.as_view(), name="tasklist-create"),
    path("task-list/list/", TaskListListView.as_view(), name="tasklist-list"),
    path(
        "task-list/update/<int:pk>/",
        TaskListUpdateView.as_view(),
        name="tasklist-update",
    ),
    path(
        "task-list/delete/<int:pk>/",
        TaskListDeleteView.as_view(),
        name="tasklist-delete",
    ),
]
