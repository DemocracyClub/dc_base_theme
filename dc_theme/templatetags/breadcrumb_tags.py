from django import template

register = template.Library()


@register.inclusion_tag("includes/_breadcrumb.html")
def breadcrumb_item(url, name, position):
    return {
        "url": url,
        "name": name,
        "position": position,
    }
