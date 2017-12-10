from django.test import TestCase
from volatile_messages import models
from django.contrib.auth.models import User


class MessageTest(TestCase):
    def test_str(self):
        msg = models.Message.objects.create(title='foo')
        self.assertEqual(str(msg), 'foo')

    def test_get_raw_content(self):
        msg = models.Message.objects.create(title='foo',
                                            content='bar')
        content = msg.get_content()
        self.assertEqual(msg.content, content)

    def test_get_content_by_template_with_title(self):
        msg = models.Message.objects.create(title='foo-template')
        content = msg.get_content()
        self.assertIn('This is a template', content)

    def test_get_content_not_found(self):
        msg = models.Message.objects.create(title='bar-template')
        content = msg.get_content()
        self.assertIn('No content', content)

    def test_read(self):
        user = User.objects.create(username='foo')
        msg = models.Message.objects.create(title='bar')
        msg.read(user)
        self.assertTrue(msg.read_by.filter(id=user.id).exists())
        self.assertTrue(msg.is_read_by(user))
