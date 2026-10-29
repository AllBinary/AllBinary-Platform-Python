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

from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor


class UpdateMyFontProcessor(MyFontProcessor):

    def _init_fields(self) -> None:
        self.updateMeasurementProcessor: UpdateMyFontInterface = None
    

    def __init__(self, keyValueDrawCharArray: UpdateMyFontInterface) -> None:
        super().__init__()
        self._init_fields()
        self.updateMeasurementProcessor = keyValueDrawCharArray
    

    def process(self, graphics: Graphics) -> None:
        self.updateMeasurementProcessor.updateMeasurement(graphics)
# from javax.microedition.lcdui.Graphics import Graphics


