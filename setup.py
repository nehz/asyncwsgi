# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='asyncwsgi',
    version='0.1.0',
    author='Zhen Wang',
    author_email='mail@zhenwang.info',
    py_modules=['asyncwsgi'],
    url='https://github.com/nehz/asyncwsgi',
    download_url='https://github.com/nehz/asyncwsgi/archive/asyncwsgi-0.1.0.tar.gz',
    license='MIT',
    description='Async WSGI support for tornado and asyncio',
    long_description=open('README.rst').read(),
    install_requires=[
        'greenlet >= 0.4.5',
    ],
)
