Phoebus Documentation
=====================

Documentation for https://github.com/shroffk/phoebus

View latest snapshot at http://phoebus-doc.readthedocs.io

To build local copy, you need to install sphinx
```
   # Standard way
   pip install Sphinx

   # Some RedHat setups
   sudo yum install python-sphinx
```

Then build the web version:
```
   make clean html
```

which creates document tree starting with `build/html/index.html`. 


Top-Level Documentation
-----------------------

The files in `phoebus-doc/source`, starting with `index.rst`,
represent the top-level documentation.

For ReStructured Text reference, see http://www.sphinx-doc.org/en/stable/rest.html



Application Documentation
-------------------------

Phoebus source code can contribute files which will be included
in an "Applications" section of the top-level documentation.

If the phoebus source code is checked out as `../phoebus`, all `../phoebus/**/doc/index.rst`
files will be added to the ``source/applications.rst`` so they're translated and included in the manual.

In addition, the content of all `../phoebus/**/doc/html` folders is copied into the manual,
so the index.rst may refer to it via ``raw`` directives.

Check `createAppIndex()` and `createPreferenceAppendix()` in source/conf.py for details,
and see `app/display/editor/doc` for example.



