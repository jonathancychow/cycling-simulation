#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name='cycling.model',
    description="Model to simulate performance for cycling time trial",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'serve-app=cycling.model.frontend.serve:main',
            'serve-production=cycling.model.frontend.serve:production'
        ]
    },
    package_data={
        'cycling.model.frontend': ['assets/*', 'assets/img/*'],
        'cycling.model': ['data/*.csv']
    },
    include_package_data=True,
    zip_safe=False,
    keywords='cycling.model',
    python_requires=">=3.7.*",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7'
    ],
    data_files=[('', ['README.md',
                      'requirements.txt',
                      ]),
                ],
)
