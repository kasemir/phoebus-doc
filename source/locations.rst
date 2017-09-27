.. _locations:

Locations
=========

Phoebus uses the following Java System properties
to locatehelp files, saved state etc.

These system variables are typically set automatically
as described below, but when necassary they can be
set when starting the product.

``phoebus.install``:
   Location where phoebus is installed.
   Has subdirectories ``lib/``, ``doc/``,
   and is used to locate the online help.
   Is automatically derived from the location
   of the framework JAR file.

``phoebus.user``:
   Location where phoebus keeps the memento
   and preferences.
   Defaults to ``.phoebus`` in the user's home directory.
