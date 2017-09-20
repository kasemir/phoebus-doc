Starting Phoebus
================

For build instructions, refer to the README.md on https://github.com/shroffk/phoebus

For pre-built binaries:
TODO, need to publish the result of ``ant dist`` somewhere.

From the command-line, invoke ``phoebus.sh -help``::

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
    -app "probe:?pvs?pv_name1,pv_name2"     -  launch an application with input arguments
    -resource  /tmp/example.plt             -  open a application configuration file with the default application
    -server port                            -  Create instance server on given TCP port
    
    Remaining arguments are names of resources to open in associated application.
    
    In 'server' mode, first instance opens UI.
    Additional calls to open resources are then forwarded to the initial instance.


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
