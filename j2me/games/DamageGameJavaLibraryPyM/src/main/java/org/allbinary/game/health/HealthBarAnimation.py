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

from org.allbinary.animation.Animation import Animation


class HealthBarAnimation(Animation):

    def _init_fields(self) -> None:
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.x2: int = 0
        self.thickness: int = 0
        self.location: int = None
        self.allbinaryLayer: AllBinaryLayer = None
    

    def __init__(self, layerInterface: AllBinaryLayer, location: int) -> None:
        super().__init__()
        self._init_fields()
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
        basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
        if self.location == basicHudFactory.TOPLEFT:
            return self.allbinaryLayer.getViewPosition().getY() - 4
        elif self.location == basicHudFactory.BOTTOMLEFT:
            return self.allbinaryLayer.getViewPosition().getY2() + 4
        return -1
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


