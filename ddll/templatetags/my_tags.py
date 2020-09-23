from django.template.defaulttags import register
# from django import template
# from django.utils.safestring import mark_safe

# register = template.Library()  # register的名字是固定的,不可改变


@register.filter
def get_item(dic, key):
    return dic.get(key)

# @register.filter
# def filter_multi(v1):
#
#     msg= v1.pop()
#     return msg
#
#
# @register.simple_tag
# def simple_tag_multi(v1, v2):
#     return v1 * v2
#
#
#
#
# @register.simple_tag
# def my_input(id,):
#     result = "<input type='text' id='%s' />" % (id)
#     return mark_safe(result)