# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "asposecellscloud"
VERSION = "18.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "asposestoragecloud"]

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.Cells.Cloud for Python",
    author="Nick Liu",
    author_email="nick.liu@aspose.com",
    url="https://github.com/aspose-cells-cloud/aspose-cells-cloud-python",
    keywords=["aspose", "cells", "cloud"],
    install_requires=REQUIRES,
    packages=['asposecellscloud', 'asposecellscloud.apis', 'asposecellscloud.models'],
    include_package_data=True,
    long_description="Aspose.Cells Cloud SDK for Python allows you to use Aspose.Cells APIs in your Python applications",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
