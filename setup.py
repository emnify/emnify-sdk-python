# coding: utf-8
from setuptools import setup, find_packages

NAME = "emnify-python-sdk"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="emnify-python-sdk",
    author_email="",
    url="",
    keywords=["Swagger", "EMnify Python SDK"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Rest API resources of the EMnify System. 
    """
)
