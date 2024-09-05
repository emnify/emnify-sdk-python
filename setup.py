# coding: utf-8
from setuptools import setup, find_packages
import os

NAME = os.getenv('PYPI_PACKAGE_NAME') or "emnify-sdk"
VERSION = "0.3.8"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ['requests', 'pydantic>=1.9.0,<2.0.0']
if __name__ == '__main__':
    with open('README.md', "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setup(
        name=NAME,
        version=VERSION,
        description="Supply your swarm of IoT Devices with cloud connectivity by EMnify. Automate your routines with this SDK for Python.",
        author="EMnify",
        author_email="",
        url="https://github.com/EMnify/emnify-sdk-python",
        keywords=["Swagger", "EMnify Python SDK", "IoT"],
        project_urls={
            "Bug Tracker": "https://github.com/EMnify/emnify-sdk-python",
        },
        install_requires=REQUIRES,
        python_requires=">=3.6",
        packages=find_packages(exclude=['tests']),
        include_package_data=True,
        long_description=long_description,
        long_description_content_type='text/markdown'
    )
