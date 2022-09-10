from setuptools import find_packages, setup

setup(
    name='bazaarpy',
    packages=find_packages(include=['bazaarpy']),
    version='0.1',
    description='A Python wrapper for the Hypixel Skyblock Bazaar API',
    author='PuffCode',
    license='GPL-3.0',
    install_requires=['requests'],
    include_package_data=True,
    package_data={'': ['*.json']}
)