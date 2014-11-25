from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='manufacture_costing',
    version=version,
    description='App for calculating GSI actual costing in manufacturing',
    author='Bobzz',
    author_email='bobzz.zone@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
