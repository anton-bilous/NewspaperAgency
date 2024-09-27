from django.template import Library


register = Library()


@register.filter
def join_as_strings(collection, delim):
    return delim.join(map(str, collection))
