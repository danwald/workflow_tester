#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages
from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = (
    'Click>=8.0',
    'fastapi>=0.95.1',
    'pydantic>=1.10.7',
    'requests>=2.30.0',
    'uvicorn>=0.22.0',
)

test_requirements = [
    'pytest>=3',
]

setup(
    author="danny crasto",
    author_email='danwald79@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="tests workflow",
    entry_points={
        'console_scripts': [
            'receiver==workflow_tester.receiver:main',
            'sender==workflow_tester.sender:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='workflow_tester',
    name='workflow_tester',
    packages=find_packages(include=['workflow_tester', 'workflow_tester.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/danwald/workflow_tester',
    version='0.1.0',
    zip_safe=False,
)
