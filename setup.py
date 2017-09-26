#!/usr/bin/env python
#
# Create source/applications.py
# by listing links to all source/applications/**/index.rst
#
# Invoked by 'generate' step in Makefile,
# also automatically invoked by
# http://docs.readthedocs.io/en/latest/builds.html
# as
#   python setup.py install

from os import walk, path


with open('source/applications.rst', 'w') as out:
    out.write("""Applications
============

The following sections describe details of specific application features.

.. toctree::
   :maxdepth: 1

""")
    for (dirpath, dirnames, filenames) in walk('source/applications'):
        for filename in filenames:
            if filename == 'index.rst':
                file = path.join(dirpath.replace("source/", ""), filename.replace(".rst", ""))
                out.write("   " + file + "\n")



