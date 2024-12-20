# Custom Template Tags for Todo App
from django import template

register = template.Library()


# Comma seperated string to list
@register.filter
def comma_seperated_to_list(value):
    return value.split(",")
