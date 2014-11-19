# -*- coding: utf-8 -*-

# bla bla, license
from setuptools import setup, find_packages
from moscow_metro import __version__


try:
    readme = open('README.md').read()
except:
    readme = 'Moscow metro for django'

setup(
    name='django-moscow-metro',
    version=__version__,
    description='Moscow metro for django',
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
