# This PostProcessing Plugin script is released 
# under the terms of the AGPLv3 or higher

from ..Script import Script
from UM.Logger import Logger

# NOTES:
#   - cura displays layers 1-indexed, but gcode labels them 0-indexed

class SimplePause(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Simple Pause",
            "key": "SimplePause",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "layer_number":
                {
                    "label": "Layer",
                    "description": "The layer to pause before. Indexed at 1. Specify multiple color changes with a comma.",
                    "unit": "",
                    "type": "str",
                    "default_value": "1"
                }
            }
        }"""

    def execute(self, data: list):

        """data is a list. Each index contains a layer"""
        layer_nums = self.getSettingValueByKey("layer_number")

        color_change = '''
;;; start simple_pause
; home x and y axes
G28 Y0 X0
; stop (bed and extruder stay at temp)
M0
;;; end simple_pause
'''[1:-1]

        Logger.log("w", 'simple_pause: number of layers ' + str(len(data)))

        layer_targets = layer_nums.split(',')
        if len(layer_targets) > 0:
            for layer_num in layer_targets:
                layer_num = int( layer_num.strip() )
                if layer_num < len(data):
                    layer = data[ layer_num ]
                    lines = layer.split("\n")
                    Logger.log("w", "simple_pause: layer " + str(layer_num) + " " + ' '.join(lines[0:4]))
                    lines.insert(0, color_change )
                    final_line = "\n".join( lines )
                    data[ layer_num ] = final_line

        return data
