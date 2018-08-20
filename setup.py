#!/usr/bin/env python

import os
import time
import io


def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding='utf-8').read().strip()
    return contents


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
    long_description=read('README.md'),
    url='https://github.com/OriHoch/python-hebrew-numbers',
    license='MIT',
    packages=('hebrew_numbers',),
    install_requires=['PyYaml'],
    package_data={
        'hebrew_numbers': ['../hebrew-special-numbers-default.yml']
    }
)
