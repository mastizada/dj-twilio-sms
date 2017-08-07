#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = "2.1.0"

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    README = f.read()

# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="dj-twilio-sms",
    version=version,
    packages=find_packages(exclude=['example.*', 'example']),
    include_package_data=True,
    license="MIT",
    description="Twilio SMS Integration for Django",
    long_description=README,
    keywords='django twilio sms',
    url="https://github.com/mastizada/dj-twilio-sms",
    author="Emin Mastizada",
    author_email="emin@linux.com",
    download_url="https://github.com/mastizada/dj-twilio-sms/zipball/master",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        "Django",
        "djangorestframework>=2.4.7",
        "twilio>=5.6.0",
    ],
)
