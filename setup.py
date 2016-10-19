#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

version = "0.3.0"

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name="dj-twilio-sms",
    version=version,
    description="Twilio SMS Integration for Django",
    license="MIT",

    author="Emin Mastizada",
    author_email="emin@mastizada.com",

    url="https://github.com/mastizada/dj-twilio-sms",
    download_url="https://github.com/mastizada/dj-twilio-sms/zipball/master",

    long_description=readme,

    package_dir={"dj_twilio_sms": "src"},
    packages=["dj_twilio_sms"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        "Django",
        "djangorestframework>=2.4.7",
        "twilio>=5.6.0",
    ]
)
