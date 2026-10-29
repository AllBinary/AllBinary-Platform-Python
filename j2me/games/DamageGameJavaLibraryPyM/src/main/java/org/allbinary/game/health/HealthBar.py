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

from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.game.health.HealthListenerInterface import HealthListenerInterface


class HealthBar(Paintable, HealthListenerInterface):

    def _init_fields(self) -> None:
        self.animationInterface: HealthBarAnimation = None
        self.healthInterface: HealthInterface = None
        self.allbinaryLayer: AllBinaryLayer = None
    

    def __init__(self, layerInterface: AllBinaryLayer, healthInterface: Health, animationInterface: HealthBarAnimation, direction: int) -> None:
        super().__init__()
        self._init_fields()
        self.allbinaryLayer = layerInterface
        self.animationInterface = animationInterface
        self.healthInterface = healthInterface
        self.healthInterface.addListener(self)
        self.onHealthChange()
    

    def onHealthChange(self) -> None:
        self.animationInterface.onHealthChange(self.healthInterface.getHealth() * self.allbinaryLayer.getWidth() / self.healthInterface.getMaxHealth())
    

    def paint(self, graphics: Graphics) -> None:
        self.animationInterface.paintXY(graphics, 0, 0)
    

    def paintThreed(self, graphics: Graphics) -> None:
        self.animationInterface.paintThreedXYZ(graphics, 0, 0, 0)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


