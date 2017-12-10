#!/usr/bin/env python
from setuptools import setup, find_packages
import volatile_messages


def read_file(name):
    with open(name) as fd:
        return fd.read()

keywords = ['django', 'web', 'volatile_messages', 'html']

setup(
    name='django-volatile_messages',
    version=volatile_messages.__version__,
    description=volatile_messages.__doc__,
    long_description=read_file('README.rst'),
    author=volatile_messages.__author__,
    author_email=volatile_messages.__email__,
    # install_requires=read_file('requirements.txt'),
    license='BSD',
    url=volatile_messages.__url__,
    keywords=keywords,
    packages=find_packages(exclude=[]),
    include_package_data=True,
    test_suite='runtests.main',
    # tests_require=read_file('requirements-tests.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
