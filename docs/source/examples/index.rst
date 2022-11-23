Examples
--------

Basic example and precode
=========================





By default, the following code will be executed before running each code block.
This allows to use ``k3d`` and ``np``.

.. code-block:: python

   import numpy as np
   import k3d

The last command of the of ``k3d-screenshot`` code block must be the K3D
Jupyter plot:

.. k3d-screenshot::
   :context: reset
   :camera: 15, 15, 10, 0, 0, 0, 0, 0, 1

   f = lambda r, d: 5 * np.cos(r) * np.exp(-r * d)
   x, y = np.mgrid[-7:7:100j, -7:7:100j]
   r = np.sqrt(x**2 + y**2)
   z = f(r, 0.1)

   fig = k3d.plot()
   surface = surface = k3d.surface(
      z.astype(np.float32), bounds=[-7, 7, -7, 7],
      attribute=z.astype(np.float32),
      color_map=k3d.colormaps.matplotlib_color_maps.viridis)
   fig += surface

   fig


context
=======

By setting ``:context: previous``, the new code block will be executed in the
context of the previous ones. To start a new context, set ``:context: reset``.

In the following example, by setting ``:context: previous`` the previous
variables can be accessed:

.. k3d-screenshot::
   :context: previous
   :camera: 8.96, -16.7, -25.63, 0, 0, 0.63, 0.45, -0.72, 0.54

   fig


camera
======

Sometime it is useful to change the position of the camera, without showing
unnecessart code to the user. We can achieve that with the ``:camera:`` option,
which accepts a list of 9 arguments, namely:

* `x_camera`, `y_camera`, `z_camera`: the position of the camera.
* `x_target`, `y_target`, `z_target`: the target of the camera (where it is
  looking at).
* `x_z_vec`, `y_z_vec`, `z_z_vec`: the components of the vertical direction
  of the camera.

For example, the previous code block was written as:

.. code-block:: python

   .. k3d-screenshot::
      :context: previous
      :camera: 8.96, -16.7, -25.63, 0, 0, 0.63, 0.45, -0.72, 0.54

      fig


Output Types
============

By default, the extension will create the following output types: ``html``,
``small.png``, ``large.png``, ``pdf``.

The output types can be changed with the following option on ``conf.py``:

.. code-block:: python

   # here we remove "large.png" and "pdf"
   k3d_screenshot_formats = ["small.png", "html"]


Function
========

It is possible to execute a function contained on a module. The function must
return a K3D plot.

.. code-block:: python

   .. k3d-screenshot:: examples/example.py func


.. k3d-screenshot:: examples/example.py func


include-source
==============

By default, the extension will show the source code of the block being
executed. It is possible to deactive this behavior on a particular code block
by setting the ``include-source`` flag:

.. code-block:: python

   .. k3d-screenshot::
      :include-source: False

      # your code here

To deactive this behavior globally, set the following option on ``conf.py``:

.. code-block:: python

   k3d_screenshot_include_source = False



small-size and large-size
=========================

The headless browser is currently incapable of determining the dimensions of
the web page, hence proper values should be used to generate the
screenshots. The default values are:

* ``small.png`` 600, 400
* ``large.png`` 1280, 850

To change the size on a code block basis:

.. code-block:: python

   .. k3d-screenshot::
      :small-size: 700, 400
      :large-size: 1920, 1080

To set the size globally, use the following options on ``conf.py``:

.. code-block:: python

   k3d_screenshot_small_size = [700, 400]
   k3d_screenshot_large_size = [1920, 1080]


doctest
=======

When using the `doctest` syntax, we have to:

1. import the appropriate modules.
2. the last line must be an assignment to the ``myk3d`` variable, which is
   used by the extension to know what to render on the screenshot.

.. k3d-screenshot::
   :camera: 4.44, -6.29, 5.12, 0, 0, 0, -0.28, 0.42, 0.86

   >>> import k3d
   >>> import numpy as np
   >>> plot = k3d.plot()
   >>> isinstance(plot, k3d.Plot)
   True
   >>> x, y = np.mgrid[-2:2:40j, -2:2:40j]
   >>> z = np.cos(x**2 + y**2)
   >>> x, y, z = [t.flatten().astype(np.float32) for t in [x, y, z]]
   >>> positions = np.vstack([x, y, z]).T
   >>> p = k3d.plot()
   >>> points = k3d.points(positions=positions, point_size=0.1)
   >>> p += points
   >>> myk3d = p


intercept_code
==============

There might be occasions where the programmer needs to performs edits to the
code block being executed, without the final user to be aware of them.

To achieve that, a function accepting the current code and returning the
modified code must be assigned to ``k3d_screenshot_intercept_code`` in
``conf.py``.

For example:

.. code-block:: python

   def edit_current_block(code):
      # use regex and/or ast modules, or other strategies to edit the code
      return modified_code
   
   k3d_screenshot_intercept_code = edit_current_block
