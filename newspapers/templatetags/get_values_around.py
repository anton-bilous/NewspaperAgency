from django.template import Library


register = Library()


@register.filter
def get_values_around(collection, index):
    size = 3
    return collection[max(0, index - size - 1) : index + size]
