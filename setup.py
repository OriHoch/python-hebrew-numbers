#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-hebrew-numbers',
    version='0.1.0',
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    description='conversion of hebrew numbers (Gimatria)',
    packages=('hebrew_numbers',)
)
