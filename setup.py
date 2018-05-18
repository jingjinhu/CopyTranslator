#!/usr/bin/env python
# coding: utf-8
import platform
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

install_requires=['pyperclip','googletrans']
#only windows can automatically install wxpython using pip, in other OS you need to install wxpython manually.
if platform.system()=='Windows':
    install_requires.append('wxpython')

setup(
    name='CopyTranslator',
    version='0.0.0.1',
    author='Yinglin Zheng',
    author_email='admin@hypercube.top',
    description=u'Copy,Translate and paste with google translate API',
	long_description=long_description,
    keywords='translate clipboard copy',
    url='https://github.com/agentzheng/CopyTranslator',
    packages=['CopyTranslator'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'CopyTranslator=CopyTranslator.CopyTranslator:main',
        ],
    },
    project_urls={  # Optional
            'Bug Reports': 'https://github.com/agentzheng/CopyTranslator/issues',
            'Say Thanks!': 'https://saythanks.io/to/agentzheng',
            'Source': 'https://github.com/agentzheng/CopyTranslator',
    },
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.1',
	'Programming Language :: Python :: 3.2',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
],
)