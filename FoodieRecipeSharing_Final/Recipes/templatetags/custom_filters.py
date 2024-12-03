from django import template

register = template.Library()

@register.filter
def range_star(value):
    # Limit the stars to a maximum of 5
    return range(1, min(value, 5) + 1)