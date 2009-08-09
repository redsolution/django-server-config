import re
from django import template

register = template.Library()

@register.filter(name='regexp')
def filter_regexp(value):
    return re.escape(value)
