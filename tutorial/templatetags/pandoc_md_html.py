from django import template

register = template.Library()

import pypandoc as pandoc
from django.utils.safestring import mark_safe

@register.filter(is_safe=True)
def markdown(value):
    x=pandoc.convert_text(value,"html5","md")
    return mark_safe(x)

