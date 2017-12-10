from django.db import models

from django.template import defaultfilters
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.conf import settings as django_settings

try:
    from django.urls import reverse_lazy as reverse
except ImportError:
    from django.core.urlresolvers import reverse

from . import settings


@python_2_unicode_compatible
class Message(models.Model):
    title = models.SlugField(primary_key=True, verbose_name=_("title"))
    content = models.TextField(max_length=65536, blank=True, null=True, verbose_name=_("content"))
    level = models.SmallIntegerField(default=settings.DEFAULT_MESSAGE_LEVEL,
        choices=settings.MESSAGE_LEVELS.items(), verbose_name=_("level"))
    template_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("template name"))
    read_by = models.ManyToManyField(django_settings.AUTH_USER_MODEL, blank=True, verbose_name=_("read by"),
        help_text=_("Users who read this message"))

    class Meta:
        app_label = 'volatile_messages'
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        return self.title

    @property
    def tag(self):
        return self.get_level_display()

    @property
    def is_template(self):
        return not bool(self.content)

    def get_content(self):
        if self.content:
            return self.content
        template_names = ['volatile_messages/%s.html' % self.title]
        try:
            return select_template(template_names).render({
                'message': self,
            })
        except TemplateDoesNotExist:
            return _("No content, please update the message or create a template.")

    def get_preview(self):
        content = self.get_content()
        preview = defaultfilters.truncatechars_html(content, 300)
        return mark_safe(preview)
    get_preview.short_description = _("Preview")

    def is_read_by(self, user):
        return self.read_by.filter(id=user.id).exists()

    def read(self, user):
        self.read_by.add(user)
