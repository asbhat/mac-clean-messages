#!/usr/bin/env python


import maccleanmessages
import sys
from setuptools import setup

requires=[]

if sys.version_info[:2] == (2, 6):
    requires.append('argparse>=1.1')


setup(
    name='maccleanmessages',
    version=maccleanmessages.__version__,
    description='Remove macOS Messages app history (chats / texts / iMessages)',
    long_description=open('README.rst').read(),
    url='https://github.com/asbhat/mac-clean-messages',
    author='Aditya Bhat',
    author_email='aditya.s.bhat@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X'
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
        'Operating System :: MacOS :: MacOS X'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Chat',
        'Topic :: Utilities'
    ],
    keywords='mac clean messages',
    packages=['maccleanmessages'],
    install_requires=requires,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['nose'],
        'test': ['nose'],
    },
    package_data={
        'maccleanmessages': ['config/*.cfg'],
    },
    entry_points={
        'console_scripts': [
            'clean-messages=maccleanmessages.driver:main',
        ],
    },
)
