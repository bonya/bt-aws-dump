"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
import os


# http://bugs.python.org/issue8876#msg208792
# http://stackoverflow.com/questions/7719380/python-setup-py-sdist-error-operation-not-permitted
del os.link

setup(
    name='bt-aws-dump',
    # Author details
    author='Bogdan Sulima',
    author_email='bogdan.sulima@gmail.com',

    py_modules=['bwaws'],

    dependency_links=[
        'https://github.com/bonya/commandr/tarball/master'
    ],

    install_requires=[
        'boto3',
        'openpyxl',
        'commandr'
    ],
    entry_points={
        'console_scripts': [
            'bt-aws-dump=btaws:run',
        ],
    },
    zip_safe=False,
    include_package_data=True
)
