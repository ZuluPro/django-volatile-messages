import re
from django.test import TestCase
from volatile_messages.templatetags import volatile_messages as tags
from volatile_messages.models import Message
from django.contrib.auth.models import User


class GetFaviconsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='foo')

    def test_does_not_exist(self):
        html_message = tags.volatile_message('ham', self.user)
        self.assertTrue(Message.objects.exists())

    def test_first_time(self):
        message = Message.objects.create(title='ham')
        html_message = tags.volatile_message('ham', self.user)
        self.assertTrue(html_message)

    def test_twice(self):
        message = Message.objects.create(title='ham')
        html_message = tags.volatile_message('ham', self.user)
        self.assertTrue(html_message)
        # Twice
        html_message = tags.volatile_message('ham', self.user)
        self.assertFalse(html_message)

    def test_already_read(self):
        message = Message.objects.create(title='ham')
        message.read_by.add(self.user)
        html_message = tags.volatile_message('ham', self.user)
        self.assertFalse(html_message)

    def test_choose_template(self):
        html_message = tags.volatile_message('ham', self.user, 'test_template.html')
        self.assertTrue(html_message)
        self.assertIn('Title: ham', html_message)
