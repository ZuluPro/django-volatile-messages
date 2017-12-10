from django.conf import settings
from django.contrib.messages import constants as messages
from django.utils.translation import ugettext_lazy as _


def get_setting(name, default):
    name = 'FIRST_MESSAGE_' + name
    return getattr(settings, name, default)


MESSAGE_LEVELS = get_setting('MESSAGE_LEVELS', messages.DEFAULT_TAGS)
DEFAULT_MESSAGE_LEVEL = get_setting('DEFAULT_MESSAGE_LEVEL', messages.INFO)
DEFAULT_TEMPLATE = get_setting('DEFAULT_TEMPLATE', 'volatile_messages/base/message.html')
