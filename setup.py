#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':

    setup(
        name='awscli-local',
        version='0.12',
        description='Thin wrapper around the "aws" command line interface for use with LocalStack',
        author='Waldemar Hummer',
        author_email='waldemar.hummer@gmail.com',
        url='https://github.com/localstack/awscli-local',
        packages=[],
        scripts=['bin/awslocal', 'bin/awslocal.bat'],
        package_data={},
        data_files={},
        install_requires=['localstack-client'],
        extras_require={
            'v1': 'awscli',
            'v2': [
                'botocore @ git+https://github.com/boto/botocore.git@v2#egg=botocore',
                'awscli @ git+https://github.com/aws/aws-cli.git@v2#egg=awscli'
            ]
        },
        license="Apache License 2.0",
        classifiers=[
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: Apache Software License",
            "Topic :: Software Development :: Testing"
        ]
    )
