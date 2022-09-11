from setuptools import find_packages, setup

setup(
    name='bazaarpy',
    packages=find_packages(include=['bazaarpy']),
    version='0.1.3',
    description='A Python wrapper for the Hypixel Skyblock Bazaar API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='PuffCode',
    license='GPL-3.0',
    install_requires=['requests'],
    include_package_data=True,
    package_data={'': ['*.json']},
    url='https://github.com/Puffball101961/bazaar.py',
)