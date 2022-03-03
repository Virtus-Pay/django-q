#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="VirtusPay",
    author_email="joel.amaro@virtuspay.com.br",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description=readme,
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"django_q_virtus": ["py.typed"]},
    include_package_data=True,
    keywords="django_q_virtus",
    name="django_q_virtus",
    package_dir={"": "django_q"},
    setup_requires=[],
    url="https://github.com/Virtus-Pay/django-q",
    version="0.1.0",
    zip_safe=False,
)