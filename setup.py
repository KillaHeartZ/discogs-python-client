#!/usr/bin/env python

from setuptools import setup

setup(
        name='discogs-client',
        version='1.1.0',
        description='Official Python API client for Discogs',
        url='https://github.com/discogs/discogs-python-client',
        author='Discogs',
        author_email='info@discogs.com',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Communications',
            'Topic :: Utilities',
            ],
        install_requires=[
            'requests',
            ],
        py_modules=[
            'discogs_client',
            ],
        )

