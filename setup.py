#!/usr/bin/env python

import sys

from dsmrsim import __name__, __version__, __author__
try:
    from setuptools import setup, find_packages
except ImportError:
    print("DSMR simulator needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

setup(name=__name__,
      version=__version__,
      description='DSMR Simulator',
      author=__author__,
      author_email='info@wemaketotem.org ',
      url='http://wemaketotem.org/',
      license='GPLv3',
      install_requires=['jinja2', 'setuptools'],
      package_dir={'': 'dsmrsim'},
      packages=['dsmrsim'],
      package_data={},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Installation/Setup',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
      ],
      scripts=[],
      data_files=[],
      )
