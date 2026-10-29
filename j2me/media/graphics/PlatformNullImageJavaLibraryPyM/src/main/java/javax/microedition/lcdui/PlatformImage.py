# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package javax.microedition.lcdui

from __future__ import annotations



#PlatformNullImageJavaLibrary
class PlatformImage:
    

    def getImage(self, graphicsSurface2: object) -> object:
        from javax.microedition.lcdui.NullImage import NullImage
        return NullImage.NULL_IMAGE
    

    def getSurfaceWidth(self, graphicsSurface2: object, width: int) -> int:
        return width
    

    def getSurfaceHeight(self, graphicsSurface2: object, height: int) -> int:
        return height
    

    def getWidth(self, image: Image, width: int) -> int:
        return width
    

    def getHeight(self, image: Image, height: int) -> int:
        return height
    

    def getGraphics(self, graphicsSurface: object, width: int, height: int, image: Image) -> Graphics:
        raise RuntimeError()
    

    def drawImage(self, image: Image, x: int, y: int, anchor: int, g2: Graphics, g: object) -> None:
        pass
    

    def drawRegion(self, image: Image, x_src: int, y_src: int, width: int, height: int, transform: int, x_dst: int, y_dst: int, anchor: int, g: Graphics) -> None:
        pass
    

    def getRGB(self, argb: list[int], offset: int, scanlength: int, x: int, y: int, width: int, height: int, image: Image) -> None:
        pass
    

    def setRGB(self, argb: list[int], offset: int, scanlength: int, x: int, y: int, width: int, height: int, image: Image) -> None:
        pass
    

    def getData(self, image: Image) -> list[int]:
        return NullUtil.getInstance().NULL_INT_ARRAY
from org.allbinary.logic.NullUtil import NullUtil


