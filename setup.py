# -*- coding: utf-8 -*-

# bla bla, license
from setuptools import setup, find_packages
from moscow_metro import __version__


simple_description = """Russian metro models for django, \
plus the parser that fills models with actual data \
(lines numbers, lines titles, lines colors, the names of the lines, the station names) \
from various data providers (primary - Wikipedia).
"""

try:
    readme = open('README.md').read()
except:
    readme = simple_description

setup(
    name='django-moscow-metro',
    version=__version__,
    description=simple_description,
    long_description=readme,
    author='Xfenix',
    author_email='ad@xfenix.ru',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'BeautifulSoup',
        'requests',
    ],
)
