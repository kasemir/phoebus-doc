Architecture
============

.. figure:: architecture.png

    Phoebus Architecture

The fundamental phoebus architecture consists of basic **core** modules
and user-iterface related **core-ui** modules, all based on the latest
Java technology, which at this time is Java 9.

A Phoebus product may contain just one application,
for example only one of Probe, PV Tree, PV Table, Display Builder Runtime,
so you end up with several Phoebus products that each perform one function.
Alternatively, you can assemble a Phoebus product that
contains all these applications. This is allows integration between the applications,
for example via context menues that start other PV-related applications based
on the current selection.

core/applications:
   Each application feature identifies itself by implementing an application descriptior
   that describes to the Phoebus framework what the name of
   the application is, which types of resources (e.g. date files files) it might accept,
   and most importantly how to start one or more instances
   of the application.

   Phoebus locates classes that implement the ``AppDescriptor`` or ``AppResourceDescriptor``
   via Java Service Provider Interfaces (SPI).
   To create an ``AppInstance``, i.e. an application instance, the framework invokes
   the ``create()`` method of the application descriptor.
   This will typically result in a new application instance, i.e. a new tab in the UI.
   Certain applications like the job viewer will create a singleton application instance.
   
   Application modules are ``jar`` files in the ``lib/`` directory of the product.
   Adding or removing Probe, PV Tree, .. from a product
   is done by simply adding or removing the respective jar file.

core/logging:
   Based on ``java.util.logging``
   
core/preferences:
   Based on ``java.util.preferences``
   
core/persistence:
   On shutdown, the state of all windows and tabs is persisted
   in a memento file, and each ``AppDescriptor`` can also
   persist its own state.
   On startup, each window and tab is restored,
   the applications are restarted, and each application
   can restore its specific state from the memento.
 
core/jobs:
   This API allows submitting jobs based on a `JobRunnable`
   that supports progress reporting and cancellation.
 
core/pv:
   API for access to life data from Process Variables.
 
core/archive:
   API for access to archived data.
   Both the life data and the archived data use
   the same data type for each sample.
 
core-ui/docking:
   A window environment similar to a web browser.
   Each window can have multiple tabs.
   Users can move tabs between existing windows,
   or detach them into newly created windows.
   
   The top-level Java FX ``Node`` for each application's
   UI scene graph is basically a ``Tab``,
   wrapped in a Phoebus ``DockItem`` that tracks the
   ``AppInstance`` to allow it to be saved and restored.
 
core-ui/selection:
   API for publishing and monitoring a selection of
   for example PVs.
 
core-ui/toolbar:
   SPI-based API to contributing to the window toolbar.
 
core-ui/menu:
   SPI-based API to contributing to the window menu.
 
core-ui/context menu:
   SPI-based API to contributing to the application context menu.
 
core-ui/logging configuration:
   UI for configuring logging.
 
core-ui/job viewer:
   UI for viewing the progress of jobs, allowing cancellation.
 
core-ui/pv list:
   UI for viewing active PVs and their connection state.




