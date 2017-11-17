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
     -settings settings.xml                  -  Import settings from file, either exported XML or property file format
     -export_settings settings.xml           -  Export settings to file
     -list                                   -  List available application features
     -app probe                              -  Launch an application with input arguments
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

Open empty PV Table::

    phoebus.sh -app pv_table

Open a file with the appropriate application feature (PV Table in this case)::

    phoebus.sh -resource /path/to/example.pvs

The '-resource' parameter can be a URI for a file or web link::

    phoebus.sh -resource http://my.site/path/to/example.pvs

The schema 'pv://?PV1&PV2&PV3' is used to pass PV names,
and the 'app=..' query parameter picks a specific app for opening the resource.

Open probe with a PV name::

    phoebus.sh -resource pv://?sim://sine&app=probe              


Open PV Table with some PVs::

    phoebus.sh -resource pv://?MyPV&pv=AnotherPV&pv=YetAnotherPV&app=pv_table              

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


Linux Installation with File Browser Integration
------------------------------------------------

This example builds and installs the distribution in ``/opt/phoebus``,
creates a user-specific *server* launcher,
and integrates that with the file browser.

First build and install Phoebus::

   ant dist
   sudo unzip -d /opt phoebus-product/target/phoebus-0.0.1.zip
   sudo ln -s /opt/phoebus-0.0.1 /opt/phoebus

Based on the generic launcher, create a copy for the user::

   mkdir -p $USER/bin
   cp /opt/phoebus/phoebus.sh $USER/bin/phoebus

Edit the user's laucher file to include the path to your Java 9 setup
and enable the 'server' mode, using a unique port for that user::

   #!/bin/sh
   # File $USER/bin/phoebus
   TOP="/opt/phoebus"
   export JAVA_HOME=/opt/jdk-9
   export PATH="$JAVA_HOME/bin:$PATH"
   java -jar ${TOP}/product-0.0.1.jar -server 4918 "$@" &

To test, run ``phoebus`` and assert that the product starts up.
Open a PV Table, add a PV name, close the PV Table and follow
the prompt to save the file as "/tmp/example.pvs".
Now run ``phoebus -resource /tmp/example.pvs``.
If Phoebus was not already running, it should start the product.
Then it opens the table in the one and only instance.

Register the MIME types supported by Phoebus applications.
This will for example register the MIME type ``application/pvtable``
for files with the ``*.pvs`` extension::

   sudo cp /opt/phoebus/phoebus.xml /usr/share/mime/packages
   sudo update-mime-database /usr/share/mime

Register the user's launcher with the Linux desktop::
 
   cp /opt/phoebus/phoebus.desktop ~/.local/share/applications/
   # Edit the file so that the 'Exec' entry
   # contains the full path to $HOME/bin/phoebus,
   # for example
   #  
   # Exec=/home/xyz/bin/phoebus -resource %f
   gedit ~/.local/share/applications/phoebus.desktop

Associate the files supported by Phoebus with the product in ~/.config/mimeapps.list::

   [Added Associations]
   application/pvtable=phoebus.desktop;
   
When you now open a new GNOME ``nautilus`` file browser, you can double-click
on ``*.pvs`` files and they open in Phoebus.
In addition, you may copy that ``*.desktop`` file to the ``~/Desktop`` folder
to offer a desktop link.


 
