from django import template

import markdown2

from activities.models import Available

register = template.Library()


@register.simple_tag
def newest_available():
    """ Gets the most recent user who have reserved. """
    available = Available.objects.all()
    return available.latest('date_end')

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to html"""
    html_body = markdown2.markdown(markdown_text)
    return html_body
