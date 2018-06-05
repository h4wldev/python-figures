# -*- coding: utf-8 -*-
"""
    python-figures
    ~~~~~
    Can use unicode symbols on any OS!
    
    :copyright: (C) 2018 h4wldev@gmail.com
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages


__version__ = '1.0'


setup(
    name='python-figures',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    license='MIT',
    author='Junho Kim',
    author_email='h4wldev@gmail.com',
    description='😀 Can use unicode symbols on any OS!',
    long_description=open('README.md').read(),
    url='https://github.com/h4wldev/python-figures'
)
