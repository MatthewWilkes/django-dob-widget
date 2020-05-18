#!/usr/bin/env python
from setuptools import setup, find_packages

from dobwidget import VERSION


setup(
    name='django-dob-widget',
    version=VERSION,
    url='https://github.com/matthewwilkes/django-dob-widget',
    author="Matthew Wilkes",
    author_email="django-dobwidget@matthewwilkes.name",
    description=(
        "A Django date widget optimised for usability in entering dates of birth"),
    long_description_markdown_filename='README.md',
    keywords="django, widget, date",
    license=open('LICENSE').read(),
    setup_requires=['setuptools-markdown'],
    platforms=['linux'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'six',
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Topic :: Software Development :: Widget Sets'],
)
