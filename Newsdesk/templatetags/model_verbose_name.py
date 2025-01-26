from django import template

register = template.Library()


@register.filter(name="model_verbose_name")
def model_verbose_name(form):
    return form._meta.model._meta.verbose_name
