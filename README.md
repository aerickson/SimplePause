# Simple Pause

A Cura 3 Post Processing Script for the Post Processing Plugin.

At the requested layers, the script will insert GCode to home the X and Y axes (G28 Y0 X0) and pause (M0). The bed and exturder are kept at temperature.

## Why

I had issues with the included plugins. On my printer (Lulzbot Mini 1), Z raises seemed to cause the print to resume above the last layers by several millimeters.

## Installation

In OS X's Finder, right click on the Cura application. Click 'Show Package Contents'. Navigate to Contents/Resources/cura/plugins/PostProcessingPlugin/scripts and copy the script there. 

In OS X's terminal:

```
cp SimplePause.py /Applications/<CURA APP>/Contents/Resources/cura/plugins/PostProcessingPlugin/scripts/
```

## Credits

Based on the included "Color Change" script.

