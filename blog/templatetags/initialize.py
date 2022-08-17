from django import template
register = template.Library()
@register.filter(name='keyInitialize')
def keyInitialize(dict,key):
    return dict.get(key)
