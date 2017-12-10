Django Volatile Messages
========================

.. image:: https://api.travis-ci.org/ZuluPro/djang-volatile-messages.svg
        :target: https://travis-ci.org/ZuluPro/djang-volatile-messages

.. image:: https://coveralls.io/repos/ZuluPro/djang-volatile-messages/badge.svg?branch=master&service=github
        :target: https://coveralls.io/github/ZuluPro/djang-volatile-messages?branch=master

Django Volatile Message is a project that aiming to provide a volatile message
app. Helping to include 1st message for user discovering a frontend.

Install & usage
===============

::

  pip install django-volatile-messages

Add the following things in your ``settings.py``: ::

  INSTALLED_APPS = (
      ...
      'volatile_messages',
      ...
  )

Contributing
============

All contribution are very welcomed, propositions, problems, bugs and
enhancement are tracked with `GitHub issues`_ system and patch are submitted
via `pull requests`_.

We use `Travis`_ coupled with `Coveralls`_ as continious integration tools.

.. _`Read The Docs`: http://djang-volatile-messages.readthedocs.org/
.. _`GitHub issues`: https://github.com/ZuluPro/djang-volatile-messages/issues
.. _`pull requests`: https://github.com/ZuluPro/djang-volatile-messages/pulls
.. _Travis: https://travis-ci.org/ZuluPro/djang-volatile-messages
.. _Coveralls: https://coveralls.io/github/ZuluPro/djang-volatile-messages
