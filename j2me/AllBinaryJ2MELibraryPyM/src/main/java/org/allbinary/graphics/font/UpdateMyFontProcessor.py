# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot 
#   
# Generated Code Do Not Modify
# package org.allbinary.graphics.font

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor


@java_inherited_overloads
class UpdateMyFontProcessor(MyFontProcessor):
    def _java_defaults(self):
        vars(self).setdefault("updateMeasurementProcessor", None)

    def _init_fields(self) -> None:
        if "updateMeasurementProcessor" not in vars(self): self.updateMeasurementProcessor: UpdateMyFontInterface = None
    

    def __init__(self, keyValueDrawCharArray: UpdateMyFontInterface) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.updateMeasurementProcessor = keyValueDrawCharArray
    

    def process(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.updateMeasurementProcessor.updateMeasurement(graphics)
# from javax.microedition.lcdui.Graphics import Graphics


