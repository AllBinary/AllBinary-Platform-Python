# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer.item

from __future__ import annotations

from org.allbinary.graphics.form.item.ABCustomImageItem import ABCustomImageItem


class LayerInterfaceFactoryImageItem(ABCustomImageItem):

    def _init_fields(self) -> None:
        self.animationArray: list[Animation] = None
        self.layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface = None
    

    def __init__(self, label: str, img: Image, layout: int, altText: str, basicColor: BasicColor, animationArray: list[Animation], layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> None:
        super().__init__(label, img, layout, altText, basicColor, 0)
        self._init_fields()
        self.animationArray = animationArray
        self.layerInterfaceFactoryInterface = layerInterfaceFactoryInterface
    

    def getLayerInterfaceFactoryInterface(self) -> LayerInterfaceFactoryInterface:
        return self.layerInterfaceFactoryInterface
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        super().paintXY(graphics, x, y)
        index = len(self.animationArray)
        while (index := index - 1) >= 0:
            self.animationArray[index].paintXY(graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface


