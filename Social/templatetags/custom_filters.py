
from django import template

register = template.Library()

@register.filter
def endswith_any(value, suffixes):
    if not value:
        return False
    suffixes_list = [s.strip().lower() for s in suffixes.split(',') if s.strip()]
    return any(value.lower().endswith(suf) for suf in suffixes_list)