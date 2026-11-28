#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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
# package org.allbinary.game.health

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.Animation import Animation


@java_inherited_overloads
class HealthBarAnimation(Animation):
    def _java_defaults(self):
        vars(self).setdefault("basicColorFactory", None)
        vars(self).setdefault("x2", 0)
        vars(self).setdefault("thickness", 0)
        vars(self).setdefault("location", 0)
        vars(self).setdefault("allbinaryLayer", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        if "x2" not in vars(self): self.x2: int = 0
        if "thickness" not in vars(self): self.thickness: int = 0
        if "location" not in vars(self): self.location: int = 0
        if "allbinaryLayer" not in vars(self): self.allbinaryLayer: AllBinaryLayer = None
    

    def __init__(self, layerInterface: AllBinaryLayer, location: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__()
        __class__._init_fields(self)
        self.allbinaryLayer = layerInterface
        self.location = location
        basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
        if self.location != basicHudFactory.TOPLEFT and self.location != basicHudFactory.BOTTOMLEFT:
            raise Exception("Location Not Valid")
        if layerInterface.getWidth() > 40:
            self.thickness = 3
        elif layerInterface.getWidth() > 20:
            self.thickness = 2
        else:
            self.thickness = 1
    

    def onHealthChange(self, newX2: int) -> None:
        self.x2 = newX2
        quarter: int = (self.allbinaryLayer.getWidth() >> 2)
        if self.x2 > quarter * 3:
            self.basicColor = self.basicColorFactory.GREEN
            self.colorP = int(self.basicColor)
        elif self.x2 > quarter * 2:
            self.basicColor = self.basicColorFactory.YELLOW
            self.colorP = int(self.basicColor)
        elif self.x2 > quarter:
            self.basicColor = self.basicColorFactory.ORANGE
            self.colorP = int(self.basicColor)
        else:
            self.basicColor = self.basicColorFactory.RED
            self.colorP = int(self.basicColor)
    

    def getY(self) -> int:
        from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
        basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
        if self.location == basicHudFactory.TOPLEFT:
            return self.allbinaryLayer.getViewPosition().getY() - 4
        elif self.location == basicHudFactory.BOTTOMLEFT:
            return self.allbinaryLayer.getViewPosition().getY2() + 4
        return -1
# from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


