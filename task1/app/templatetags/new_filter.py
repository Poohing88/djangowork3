from django import template


register = template.Library()


@register.filter
def color(number):
    try:
        num = float(number)
        if num <= 0:
            number = num
        elif 0 < num <= 1:
            number = num
        elif 1 < num <= 2:
            number = num
        elif 2 < num <= 5:
            number = num
        elif 5 < num < 1900:
            number = num
        else:
            return number
        return number
    except:
        return number
