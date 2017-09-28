Preference Settings
===================

When you run Phoebus, you may find that it cannot connect to your control system
because for example the EPICS Channel Access address list is not configured.

To locate available preferences, look file files named ``*preferences.properties``
in the source code, for example in the PV Table application::

   # ----------------------------------------
   # Package org.phoebus.applications.pvtable
   # ----------------------------------------

   # Show a "Description" column that reads xxx.DESC?
   show_description=true


Create a file ``settings.ini`` that lists the settings you want to change::

   # Format:
   #
   #  package_name/setting=value

   org.phoebus.applications.pvtable/show_description=false


 Start Phoebus like this to import the settings from your file::

  phoebus.sh -settings /path/to/settings.ini


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

In your code, create a ``preferences.properties`` file that lists the available settings::

   # -------------------------------------------------------
   # Package org.phoebus.applications.my_application_feature
   # -------------------------------------------------------

   # Explain what this setting means,
   # what values are allowed etc.
   my_setting=SomeValue


Load that as the default, then read the ``java.util.prefs.Preferences`` like this::


    import org.phoebus.framework.preferences.PreferencesReader;
    final PreferencesReader prefs = new PreferencesReader(getClass(), "/preferences.properties");
    
    String pref1 = prefs.get("my_setting");
    Boolean pref2 = prefs.getBoolean("my_other_setting");
    // .. use getInt, getDouble as needed

By default, the user settings are stored in a ``.phoebus`` folder
in the home directory.
This location can be changed by setting the Java property ``java.util.prefs.userRoot``.

In the future, a preference UI might be added, but as mentioned
the preference settings are not meant to be adjusted by end users.
