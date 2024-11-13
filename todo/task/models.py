from django.db import models
from frame.models import BaseModel


class Task(BaseModel):
    task_name = models.CharField(max_length=200, null=True)
    task_description = models.TextField(null=True)
    task_tag = models.ManyToManyField("Tag", null=True)

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Task",
            "list_title": "Tasks",
            "create_title": "Create Task",
            "enable_search": True,
            "default_sort_by": "task_name",
            "list_url": "task-list",
            "navigation": True,
            "fields": [
                {
                    "name": "task_name",
                    "display_name": "Task Name",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "task_description",
                    "display_name": "Task Description",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "task_tags",
                    "display_name": "Task Tags",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
            ],
            "actions": {
                "button": [
                    {"name": "Create", "url": "task-create", "disabled": ["detail"]}
                ],
                "dropdown": [
                    {"name": "Details", "url": "task-detail", "disabled": ["detail"]},
                    {"name": "Edit", "url": "task-update"},
                    {"name": "Delete", "url": "task-delete"},
                ],
            },
        }


class Tag(BaseModel):
    tag_name = models.CharField(max_length=200, null=True)

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Tag",
            "list_title": "Tags",
            "create_title": "Create Tag",
            "enable_search": True,
            "default_sort_by": "tag_name",
            "list_url": "tag-list",
            "navigation": True,
            "fields": [
                {
                    "name": "tag_name",
                    "display_name": "Tag Name",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "task_tags",
                    "display_name": "Task Tags",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "task",
                    "display_name": "Task",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
            ],
            "actions": {
                "button": [
                    {"name": "Create", "url": "tag-create", "disabled": ["detail"]}
                ],
                "dropdown": [
                    {"name": "Details", "url": "tag-detail", "disabled": ["detail"]},
                    {"name": "Edit", "url": "tag-update"},
                    {"name": "Delete", "url": "tag-delete"},
                ],
            },
        }
