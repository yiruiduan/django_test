#!/usr/bin/python
#auth:yiruiduan
from django import template
from django.utils.safestring import mark_safe

register=template.Library()

@register.simple_tag()
def add_fun(a1,a2):
    return a1+a2