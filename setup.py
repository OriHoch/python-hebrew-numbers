#!/usr/bin/env python

import os, time

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if os.path.exists("VERSION.txt"):
    # this file can be written by CI tools (e.g. Travis)
    with open("VERSION.txt") as version_file:
        version = version_file.read().strip().strip("v")
else:
    version = str(time.time())
    
setup(
    name='python-hebrew-numbers',
    version=version,
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    description='conversion of hebrew numbers (Gimatria)',
    packages=('hebrew_numbers',)
)
