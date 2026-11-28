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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.form.item.ABCustomImageItem import ABCustomImageItem


@java_inherited_overloads
class LayerInterfaceFactoryImageItem(ABCustomImageItem):
    def _java_defaults(self):
        vars(self).setdefault("animationArray", None)
        vars(self).setdefault("layerInterfaceFactoryInterface", None)

    def _init_fields(self) -> None:
        if "animationArray" not in vars(self): self.animationArray: list[Animation] = None
        if "layerInterfaceFactoryInterface" not in vars(self): self.layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface = None
    

    def __init__(self, label: str, img: Image, layout: int, altText: str, basicColor: BasicColor, animationArray: list[Animation], layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface
        super().__init__(label, img, layout, altText, basicColor, 0)
        __class__._init_fields(self)
        self.animationArray = animationArray
        self.layerInterfaceFactoryInterface = layerInterfaceFactoryInterface
    

    def getLayerInterfaceFactoryInterface(self) -> LayerInterfaceFactoryInterface:
        from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface
        return self.layerInterfaceFactoryInterface
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintXY", graphics, x, y)
        index = len(self.animationArray)
        while (index := index - 1) >= 0:
            self.animationArray[index].paintXY(graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface


