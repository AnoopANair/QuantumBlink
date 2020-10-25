from setuptools import setup
import setuptools

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="QuantumBlink",
    version="1.0.0",
    description="A Python package to flouresence intermittency data of quantum dots",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AnoopANair/QuantumBlink",
    author="Anoop A Nair {K.G.T. group}",
    author_email="mailtoanoop71@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)


