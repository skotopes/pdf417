#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name='pdf417',
    version='0.8.1',
    description='PDF417 2D barcode generator for Python',
    long_description=long_description,
    author='Ivan Habunek',
    author_email='ivan.habunek@gmail.com',
    url='https://github.com/mosquito/pdf417/',
    keywords='pdf417 2d barcode generator',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['pdf417'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pdf417gen=pdf417.console:main',
        ],
    },
    extras_require={
        "pillow-simd": [
            'Pillow-SIMD>=2;python_version>="3"',
            'Pillow-SIMD>=2,<4;python_version<"3"',
        ],
        "pillow": [
            'Pillow>=2;python_version>="3"',
            'Pillow>=2,<4;python_version<"3"',
        ],
        ':python_version < "3"': ['future'],
    }
)
