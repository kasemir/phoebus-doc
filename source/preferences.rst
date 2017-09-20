Preference Settings
===================

When you run Phoebus, you may find that it cannot connect to your control system
because for example the EPICS Channel Access address list is not configured.

 1) Exit Phoebus
 2) Start Phoebus as ``phoebus.sh -export_settings /path/to/my_settings.xml``
 3) Edit the exported file.
    For example, find the ``addr_list`` entry and set it to the desired value::

         <entry key="addr_list" value="127.0.0.1 my_ca_gateway.site.org:5066"/>
 4) Start Phoebus as ``phoebus.sh -settings /path/to/my_settings.xml``


Conceptually, preference settings are meant to hold critical configuration
parameters like the control system network configuration.
They are configured by system administrators, and once they are properly adjusted
for your site, there is usually no need to change them.

Most important, these are not settings that an end user would need to see
and adjust during ordinary use of the application.
For such runtime settings, each applicaition needs to offer user interface options
like context menus or configuration dialogs.


.. _preferences-notes:

Developer Notes
---------------

In your code, use ``java.util.prefs.Preferences`` to read settings like this::

    import java.util.prefs.Preferences;

    final Preferences prefs = Preferences.userNodeForPackage(SomeTopLevelClassOfMyModule.class);
    String value = prefs.get("some_setting", "default_value");
    prefs.put("some_setting", value);

Note how this code pattern reads the setting, and then **writes** it.
In case the setting is not defined in the preferences,
you will thus add it to the preferences with the default value.

This way, ``-export_settings`` will export "some_setting".
Users are thus able to see the name of your setting and its default value,
edit it, and then import the desired value.
If you do not ``put`` your setting but only ``get`` it,
end users would have to refer to your source code to learn about
available settings and their default value.

By default, the user settings are stored in a ``.phoebus`` folder
in the home directory.
This location can be changed by setting the Java property ``java.util.prefs.userRoot``.

In the future, a preference UI might be added, but as mentioned
the preference settings are not meant to be adjusted by end users.
