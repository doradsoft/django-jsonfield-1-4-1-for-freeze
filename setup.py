#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-jsonfield",
    version="1.4.1",
    description="JSONField for django models",
    url="https://github.com/adamchainz/django-jsonfield",
    author="Matthew Schinckel",
    author_email="matt@schinckel.net",
    maintainer="Adam Johnson",
    maintainer_email="me@adamj.eu",
    packages=[
        "jsonfield",
    ],
    include_package_data=True,
    test_suite='tests.main',
    install_requires=[
        'Django>=1.11',
        'six',
    ],
    classifiers=[
        "Development Status :: 6 - Mature",
        'Framework :: Django',
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
