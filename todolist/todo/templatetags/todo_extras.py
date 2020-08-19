from django.template.defaultfilters import register
from todo.models import Todo


@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]


@register.filter(name="get_status_displayed")
def get_status_displayed(s):
    for status, label in Todo.STATUS_CHOICES:
        if status == s:
            return label
