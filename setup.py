"""
Package setup file.
"""

import sys
from setuptools import setup

sys.path.append('kevin/')
from __init__ import __version__

setup(name='kevin',
      version=__version__,
      description="Kevin's custom Python package.",
      url='https://kevinalyons.com',
      author='Kevin Lyons',
      author_email='kevinandrewlyons@gmail.com',
      license='MIT',
      packages=['kevin'],
      zip_safe=False,
      install_requires=[
          'numpy',
          'pandas',
          'tqdm'
      ],)
