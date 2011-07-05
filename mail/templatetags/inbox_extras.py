from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="industry_name")
@stringfilter
def industry_name_filter(value):
    #some of the industry names and party names are goofy- we can fix them here
    if value == "D":
        return "Democrat"
    elif value == "R":
        return "Republican"
    elif value == "L":
        return "Libertarian"
    elif value == "3":
        return "Third party"
    elif value == "N":
        return "No party"
    elif value == "I":
        return "Independent"
    elif value == "OTHER NON-PHYSICIAN HEALTH PRACTITIONERS":
        return "NON-PHYSICIAN HEALTH PRACTITIONERS"
    else:
        return value