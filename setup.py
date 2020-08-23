from setuptools import setup, find_packages

setup(
    name="labestia",
    version="0.1",
    packages=find_packages(),
    scripts=["scripts/labestia"],
    install_requires=["pygame==2.0.0.dev6"],
    include_package_data=True,
    author="Javier Mansilla",
)
