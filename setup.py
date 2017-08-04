"""
Package setup file.
"""

import sys
from setuptools import setup, find_packages

sys.path.append('kevin/')
from __init__ import __version__, __author__, __description__

setup(name='kevin',
      version=__version__,
      author=__author__,
      description=__description__,
      url='hhttps://github.com/kalyons11/kevin',
      author_email='kevinandrewlyons@gmail.com',
      license='MIT',
      packages=find_packages()
      )
