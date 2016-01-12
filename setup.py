# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from metro import __version__


readme = 'README.md'
try:
    import pypandoc
    read = lambda: pypandoc.convert(readme, 'rst')
except ImportError:
    import os
    read = lambda: os.path.join(
        os.path.dirname(os.path.abspath(__file__)), readme
    )


setup(
    name='django-metro',
    version=__version__,
    description="""Basic metro models for Django 1.7+, \
    plus the parser that fills models with actual data \
    (lines numbers, lines titles, lines colors, the names \
    of the lines, the station names) from various data \
    sources (primary - Wikipedia).
    """,
    long_description=read(),
    url='https://github.com/xfenix/django-metro',
    author='Denis Anikin',
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
        'Programming Language :: Python :: 3',
    ],
    zip_safe=True,
    install_requires=[
        'Django>=1.7',
        'BeautifulSoup4',
        'requests',
        'six',
    ],
)
