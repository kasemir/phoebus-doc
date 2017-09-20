Starting Phoebus
================

For build instructions, refer to the README.md on https://github.com/shroffk/phoebus

For pre-built binaries:
TODO, need to publish the result of ``ant dist`` somewhere.

From the command-line, invoke ``phoebus.sh -help``::

      _______           _______  _______  ______            _______ 
     (  ____ )|\     /|(  ___  )(  ____ \(  ___ \ |\     /|(  ____ \
     | (    )|| )   ( || (   ) || (    \/| (   ) )| )   ( || (    \/
     | (____)|| (___) || |   | || (__    | (__/ / | |   | || (_____ 
     |  _____)|  ___  || |   | ||  __)   |  __ (  | |   | |(_____  )
     | (      | (   ) || |   | || (      | (  \ \ | |   | |      ) |
     | )      | )   ( || (___) || (____/\| )___) )| (___) |/\____) |
     |/       |/     \|(_______)(_______/|/ \___/ (_______)\_______)
     
     Command-line arguments:
     
     -help                                   -  This text
     -settings settings.xml                  -  Import settings from file
     -export_settings settings.xml           -  Export settings to file
     -list                                   -  List available application features
     -app "probe?pv=pv_name1&pv=pv_name2"    -  Launch an application with input arguments
     -resource  /tmp/example.plt             -  Open an application configuration file with the default application
     -server port                            -  Create instance server on given TCP port
   
   In 'server' mode, first instance opens UI.
   Additional calls to open resources are then forwarded to the initial instance.


Command Line Parameters for Applications
----------------------------------------

To open an application feature like "probe" or the "pv_tree" from the command line,
use the following example parameters.

Open empty instance of probe::

    phoebus.sh -app probe

Open probe with a PV name::

    phoebus.sh -app probe?pv=MyPV

Open three instances of probe, each with a PV name::

    phoebus.sh -app probe?pv=MyPV&pv=AnotherPV&pv=YetAnotherPV

Open empty PV Table::

    phoebus.sh -app pv_table

Open PV Table with some PVs::

    phoebus.sh -app pv_table?pv=MyPV&pv=AnotherPV&pv=YetAnotherPV

Open PV Table for given input file::

    phoebus.sh -app pv_table?file=/path/to/example.pvs

Open a file with the appropriate application feature (PV Table in this case)::

    phoebus.sh -resource /path/to/example.pvs


Note that all these examples use the internal name of the application feature,
for example "pv_table", and not the name that is displayed the user interface,
like "PV Table".
Use the ``-list`` option to see the names of all available application features.

Server Mode
-----------

By default, each invocation of ``phoebus.sh ...`` will start a new instance,
with its own main window etc.

In a control room environment it is often advantageous to run only one instance
on a given computer.
For this scenario, invoke ``phoebus.sh`` with the ``-server`` option, using
a TCP port that you reserve for this use on that computer, for example::

   phoebus.sh -server 4918
   
The first time you start phoebus this way, it will actually open the main window.
Follow-up invocations, for example::

   phoebus.sh -server 4918 -resource /path/to/some/file.pvs

will contact the already running instance and have it open the requested file.
