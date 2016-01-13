#!/usr/bin/env python
#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import os
import sys
from setuptools import setup

setup(
    name="round-py",
    version='1.0',
    description="Python client for DockRounder.",
    author='Satoshi Konno',
    author_email='skonno@cybergarage.org',
    url='https://github.com/cybergarage/round-py',
    packages=[
        'round'
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'License :: OSI Approved :: new BSD license',
    ],    
)