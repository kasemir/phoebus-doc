Introduction
===================================

Phoebus is an update of the Control System Studio toolset
that removes dependencies on Eclipse RCP and SWT.

.. image:: phoebus_example.png
      :width: 90%

While Eclipse RCP has served CS-Studio well for about a decade,
we are beginning to experience its limitations for control system
user interface developemnt.

Key Goals of the Phoebus project:

 * Retain functionality of key CS-Studio tools,
   specifically the Display Builder, Data Browser,
   PV Table, PV Tree, Alarm UI, Scan UI, ..
   supporting their original configuration files
   with 100% compatibility.

 * Provide full control of window placement
   free from RCP restrictions.

 * Use Java FX as the graphics library to overcome
   limitations of SWT.

 * Prefer core Java functionality over external
   libraries whenever possible:
   Java FX as already mentioned,
   Java 9 modules for bundling,
   SPI for locating extensions,
   java.util for logging and preferences, ...

 * Reduce build system complexity,
   fetching external dependencies in one initial step,
   then supporting a fully standalone, reproducible
   build process.


For more, see https://docs.google.com/document/d/11W52PRlsRjpIvP81HxUxxR9g180DHDByCohYQ9TQv7U


