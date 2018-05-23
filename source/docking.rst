Window Environment
==================

When you start Phoebus for the first time, it opens a main window.
As you use the *Applications* menu to open for example Probe, the PV Tree etc.,
these all open up as new Tabs.

.. figure:: singular_tab.png

    Window with just one tab, showing that tab so you can drag it.

The behavior of these tabs is very similar to the handling of tabs
in a web browser.
You can rearrange the tabs within a window by dragging them around.
You can also drag a tab out of the window to detach it into its own window.
Alternatively, you can invoke the *detach* option from the context menu of the tab
to detach it.
Tabs can be dragged between the main window and such detached windows.

The tab context menu options to *Split Horizontally* or *Split Vertically*
will create sub-panels witin the window between which tabs can be arranged.

.. figure:: split.png

    In this example, the original PV Tree tab has been split *horizontally*,
    creating a left and right section.
    The left section contains the original PV Tree.
    A new Display Builder panel has been placed into the originally empty right section.
    Next, the PV Tree tab on the left has once more been split, this time *vertically*,
    and a new Jobs viewer has been placed in the newly created bottom half.

By default, even a window with just one tab will show that tab.
This has the advantage that you can then grab that tab to move it
into another window, or arrange tabs in the split subsections of a window.
At times, however, you may prefer to hide such singular tabs
to preserve screen space.
In the *Window* menu, select *Always show Tabs* to show respectively hide
singular tabs.

.. figure:: no_singular_tab.png

    Window with just one tab, hiding the actual tab to offer more screen space.


Saving, Restoring, Locking the Window Layout
--------------------------------------------

The current window layout is saved to a ``memento`` file when exiting the program.
This ``memento`` file is by default located within a ``.phoebus`` subdirectory of the user's home directory.
To change the location from ``$HOME/.phoebus`` to a custom location, set the Java System property ``phoebus.user`` to the desired location.

When later starting the program back up, it will load the saved window layout.

By making the ``memento`` file read-only, system administrators can prevent the program from updating the file on exit.
Each time the program is started, it will thus start out with a known window layout.

System administrators may edit a saved ``memento`` file with a text editor.
It's an XML file that reflects the saved layout via an XML tree of ``<pane>`` elements.
Adding a `fixed` option to a pane like this locks the tabs within that pane::

    <pane fixed="true">


.. figure:: lock.png

    In this example, the ``memento`` has been edited to mark the upper and lower panes on the left as ``fixed="true"``.
    Note that the tabs for the PV Tree and Active Jobs have no ``x`` to close them.
    These tabs cannot be closed, they cannot be moved to other window sections,
    and you can no longer add new tabs into these *fixed* panes.

This allows system administrators to create a default layout that contains certain fixed panes
which the user cannot accidentally delete at runtime.


