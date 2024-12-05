from django.db import models
from frame.models import BaseModel
from django.utils import timezone


class Task(BaseModel):
    PRIORITIES = [
        ("-2", "-2"),
        ("-1", "-1"),
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
    ]
    task_completed = models.BooleanField(default=False)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField(blank=True)
    task_priority = models.CharField(choices=PRIORITIES, default="0", max_length=20)
    task_tags = models.CharField(max_length=200, default="None")
    task_due_date = models.DateField(null=True)

    class Meta:
        ordering = ["task_completed", "-task_due_date", "-task_priority", "pk"]

    def is_overdue(self):
        """Return True if the task is overdue."""
        if self.task_due_date == timezone.now().date():
            return True
        return False

    @property
    def style_classes(self):
        """Return a dictionary of style classes based on task attributes."""
        classes = {
            "row": "",
            "name_cell": "",
            "date_cell": "",
            # Add more keys as needed
        }
        if self.task_completed:
            classes["row"] += " line-through"
        if self.task_due_date < timezone.now().date() and not self.task_completed:
            classes["row"] += " text-rose-500"
        if self.task_priority == "1" or self.task_priority == "2":
            classes["row"] += " font-bold"
        # Extend logic as required
        return classes

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Task",
            "list_title": "Tasks",
            "create_title": "Create Task",
            "enable_search": True,
            "default_sort_by": "pk",
            "list_url": "task-list",
            "navigation": True,
            "fields": [
                {
                    "name": "task_completed",
                    "display_name": "Task Completed",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": False,
                    "editable_in_list": True,
                },
                {
                    "name": "task_name",
                    "display_name": "Task Name",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                    "editable_in_list": True,
                },
                {
                    "name": "task_description",
                    "display_name": "Task Description",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                    "editable_in_list": True,
                },
                {
                    "name": "task_priority",
                    "display_name": "Task Priority",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                    "editable_in_list": True,
                },
                {
                    "name": "task_tags",
                    "display_name": "Task Tags",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                    "editable_in_list": True,
                    "custom_fragment": "custom_fragments/task_tags.html",
                },
                {
                    "name": "task_due_date",
                    "display_name": "Task Due Date",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                    "editable_in_list": True,
                },
            ],
            "actions": {
                "button": [
                    {"name": "Create", "url": "task-create", "disabled": ["detail"]},
                ],
                "dropdown": [
                    {"name": "Details", "url": "task-detail", "disabled": ["detail"]},
                    {"name": "Edit", "url": "task-update"},
                    {"name": "Delete", "url": "task-delete"},
                ],
            },
        }
