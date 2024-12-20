from django import template

register = template.Library()


@register.inclusion_tag('blog_prototype/sidebar.html', takes_context=True)
def blog_sidebar(context, current_section=None):
    request = context['request']

    if current_section is None:
        path = request.path_info
        path_parts = filter(lambda pp: pp != '', path.split('/'))
        current_section = path_parts[0]

    return {
        'request': request,
        'current_section': current_section,
    }
