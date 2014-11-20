# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from russian_metro import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-russian-metro',
    version=__version__,
    description="""Russian metro models for Django 1.7+, \
    plus the parser that fills models with actual data \
    (lines numbers, lines titles, lines colors, the names \
    of the lines, the station names) from various data \
    providers (primary - Wikipedia).
    """,
    long_description=read('README.md'),
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
    ],
)
