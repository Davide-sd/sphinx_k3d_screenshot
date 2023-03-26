Changelog
---------

0.2.0
=====

* Added ``k3d_screenshot_driver_options`` configuration option, which can be
  used to set an headless driver, or to request the driver to use particular
  settings.

* **Breaking:** starting from this version, by default the browser is not run
  in headless mode. User need to set 
  ``k3d_screenshot_driver_options=["--headless"]`` in the configuration file.

* Added ``k3d_screenshot_modify_driver`` configuration option.

* Better code organization.


0.1.2
=====

Added ``k3d_screenshot_camera_factor`` configuration option.


0.1.1
=====

Screenshots are now generated with K3D-Jupyter's ``k3d_remote``. It should
create more consistent results.


0.1.0
=====

Initial release.
