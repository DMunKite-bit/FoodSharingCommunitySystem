# custom_filters.py
from django import template

register = template.Library()

@register.filter
def range_star(value):
    """Returns a list of numbers from 0 to value-1"""
    return range(value)