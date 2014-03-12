#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pipsave',
    version='0.0.1',
    description='Wraps pip, manages requirements.txt',
    author='Michael Layzell (https://github.com/mystor)',
    url='https://github.com/mystor/pipsave',
    scripts=['pipsave']
)

