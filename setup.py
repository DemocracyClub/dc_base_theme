#!/usr/bin/env python3
import os

from setuptools import setup

packages = []
data_files = []
app_dir = 'dc_theme'


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way. Copied from Django.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


for dirpath, dirnames, filenames in os.walk(app_dir):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]

    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))

    elif filenames:
        data_files.append(
            [dirpath, [os.path.join(dirpath, f) for f in filenames]])


setup(
    name='DC Base Theme',
    version='0.3.12',
    description='Base assets for DC projects',
    author='Sym Roe',
    author_email='sym.roe@democracyclub.org.uk',
    packages=packages,
    package_data={'dc_theme': [
        '*.scss',
        '*.html',
        '*.js',
        '*.png',
    ]},
    include_package_data=True,
    install_requires=[
        'django-pipeline>=1.6.8,<2.0',
        'libsass==0.14.1',
        'jsmin==2.2.2',

    ],
    setup_requires=['wheel']
)
