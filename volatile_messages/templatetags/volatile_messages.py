from django import template
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _

from ..models import Message
from .. import settings

register = template.Library()


@register.simple_tag
def volatile_message(title, user, template_name=settings.DEFAULT_TEMPLATE):
    message, _ = Message.objects.get_or_create(title=title)
    if message.is_read_by(user):
        return ''

    template = get_template(template_name)
    message.read(user)
    return template.render({
        'message': message,
    })
