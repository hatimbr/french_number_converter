from setuptools import find_packages, setup

setup(
    name='frenchconverter',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'frenchconverter = french_converter:cli'
        ]
    },
)