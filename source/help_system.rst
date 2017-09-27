Help System
===========

Help files are `*.rst` files with reStructuredText markup
as described at http://www.sphinx-doc.org/en/stable/rest.html.

The main repository for help files is phoebus-doc
(for the time https://github.com/kasemir/phoebus-doc)
and a snapshot of the current version is accessible on
http://phoebus-doc.readthedocs.io.

Each phoebus application feature can contribute help content.
This is done by adding a ``doc/`` folder with an ``index.rst``
file to the application sources.
When phoebus-doc is built, it includes all ``phoebus/applications/**/doc/index.rst``
in the Applications section of the manual.
 
When the phoebus product is built,
it checks for the html version of the manual
in ``phoebus-doc/build/html``.
If found, it is bundled into the product.

Complete build steps of manual and product::

    # Obtain sources for documentation and product
    git clone https://github.com/kasemir/phoebus-doc.git
    git clone https://github.com/shroffk/phoebus.git

    cd phoebus-doc
    # Building the manual will locate and include
    # all ../phoebus/applications/**/doc/index.rst
    make html
    # Windows: Use make.bat html

    cd ../phoebus
    # Fetch dependencies
    mvn clean verify -f dependencies/pom.xml

    # Building the product will bundle
    # ../phoebus-doc/build/html
    # as phoebus-product/target/doc
    ant
    # or mvn clean install
    
    # Could now run the product via phoebus-product/phoebus.sh,
    # or ZIP for distribution
    ant dist



Internals
---------

In ``phoebus-doc/source/conf.py``, the ``createAppIndex()`` method
checks for the phoebus sources and builds the application section
of the manual.

When invoking the Phoebus ``Help`` menu,
it looks for a ``doc/`` folder in the installation location (see :ref:`locations`).

As a fallback for development in the IDE, it looks for ``phoebus-doc/build/html``.
