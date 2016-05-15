#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='djangocms-vimeo',
    version='0.3.3',
    description='Video plugin for django CMS',
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='https://github.com/nimbis/djangocms-vimeo',
    packages=find_packages(exclude=["tests", ]),
    install_requires=[
        'Django',
        'django-cms >= 3.0',
    ],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False
)
