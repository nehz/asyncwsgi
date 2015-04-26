# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='asyncwsgi',
    version='0.1.0',
    author='Zhen Wang',
    author_email='mail@zhenwang.info',
    url='https://github.com/nehz/asyncwsgi',
    license='MIT',
    description='Async WSGI support for tornado and asyncio',
    long_description=open('README.md').read(),
    install_requires=[
        'greenlet >= 0.4.5',
    ],
)
