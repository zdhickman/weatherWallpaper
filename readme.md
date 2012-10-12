README

Description
===========

This script will collect weather information from Yahoo! Weather, and change
the wallpaper based on the results. The script is written for Windows in that
a Windows .dll file is used to change the wallpaper, but this function can be
modified in order to work on a Mac or other Linux-based OS.

Wallpapers are not included, but instructions on where to add the wallpapers
is included.



How to Use
==========

This script can be manually run on its own to change the wallpaper, or it can
be used with a Scheduled Task.


General Instructions
--------------------

1. Open weatherwallpaper.cfg

2. For `location`, enter the code that appears in the URL when you view
your area's weather on [Yahoo! Weather](http://www.weather.yahoo.com).

3. For `wallpaper_path`, enter in a path to the location of your /wallpaper/
folder: by default, it is located in the same directory as the script itself.
When left blank, the default is the current directory.

4. You're now ready to use your script!



Setting Up Wallpapers
---------------------

Wallpapers are set up in the file path format of `/condition/time/wallpaper.jpg`
Simply add the wallpaper you want in the correct directory.



**NOTE**: If you are setting up this script to be used with a Scheduled Task,
and you did not specify the path in the .cfg file, make sure to add the actual
path of the script in the `Start in (optional):` field.