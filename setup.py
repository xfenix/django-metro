# -*- coding: utf-8 -*-
import os
import pypandoc
from setuptools import setup, find_packages
from russian_metro import __version__


setup(
    name='django-russian-metro',
    version=__version__,
    description="""Russian/CIS metro models for Django 1.7+, \
    plus the parser that fills models with actual data \
    (lines numbers, lines titles, lines colors, the names \
    of the lines, the station names) from various data \
    sources (primary - Wikipedia).
    """,
    long_description=lambda: pypandoc.convert('README.md', 'rst'),
    url='https://github.com/xfenix/django-russian-metro',
    author='Xfenix',
    author_email='ad@xfenix.ru',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=True,
    install_requires=[
        'Django>=1.7',
        'BeautifulSoup4',
        'requests',
        'transliterate',
    ],
)
