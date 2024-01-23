from setuptools import setup, find_namespace_packages

setup(
    name="jetphotos",
    version="0.0.1",
    python_requires='>=3',
    packages=find_namespace_packages(where='src')
)