from setuptools import setup, find_packages

setup(
    name="stats",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[pandas,numpy],
    author="Gaurav G",
    author_email="lotusheart2016@gmail.com",
    description="A package for evaluating model performance metrics",
    url="https://github.com/visit-www/stats.git",
)
