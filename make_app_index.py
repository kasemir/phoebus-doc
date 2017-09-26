#!/usr/bin/env python
#
# Create source/applications.py
# by listing links to all source/applications/**/index.rst
#
# Invoked by 'generate' step in Makefile

from os import walk, path


print """Applications
============

The following sections describe details of specific application features.

.. toctree::
   :maxdepth: 1

"""


for (dirpath, dirnames, filenames) in walk('source/applications'):
    for filename in filenames:
        if filename == 'index.rst':
            print("   " + path.join(dirpath.replace("source/", ""), filename.replace(".rst", "")))
