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

from org.allbinary.game.health.HealthBarAnimation import HealthBarAnimation


class HealthBarTwodAnimation(HealthBarAnimation):
    

    def __init__(self, layerInterface: AllBinaryLayer, location: int) -> None:
        super().__init__(layerInterface, location)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        ax: int = self.allbinaryLayer.getViewPosition().getX()
        self.basicSetColorUtil.setBasicColorP3(graphics, self.basicColor, self.colorP)
        graphics.fillRect(ax, self.getY() - 1, self.x2, self.thickness)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


