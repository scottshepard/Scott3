from setuptools import setup, find_packages

__version__ = '0.1'
__author__ = 'Scott Shepard'
__copyright__ = 'Copyright 2019 Scott Shepard'

setup(name='Scott3',
      version=__version__,
      description='Connect to S3',
      url='http://github.com/scottshepard/Scott3',
      author=__author__,
      packages=find_packages(),
      install_requires=[
            'pandas>=0.21.0',
            'boto3',
            'pyyaml'
            ]
      )
