#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


setup(
    name='pymcce',
    version='0.1.0',
    description="A suite of tools to analyze Monte Carlo simulations generated from MCCE.",
    author="Kamran Haider",
    author_email='kamranhaider.mb@gmail.com',
    url='https://github.com/kamran-haider/pymcce',
    packages=find_packages(include=['pymcce']),
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='pymcce',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)
