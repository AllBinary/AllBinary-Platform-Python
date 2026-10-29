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



class MyFontProcessor:
    instance: MyFontProcessor = None
    

    @staticmethod
    def defaultCharWidth(font: Font) -> int:
        return font.charWidth('C')
    

    @staticmethod
    def defaultStringWidth(font: Font, size: int) -> int:
        return MyFontProcessor.defaultCharWidth(font) * size
    

    @staticmethod
    def getInstance() -> MyFontProcessor:
        return MyFontProcessor.instance
    

    def process(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics


MyFontProcessor.instance = MyFontProcessor()

