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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.layer.LinePathAnimation import LinePathAnimation


class LinePathRelativeAnimation(LinePathAnimation):
    instanceC: LinePathRelativeAnimation = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> LinePathAnimation:
        return LinePathRelativeAnimation.instanceC
    

    def paint(self, graphics: Graphics, point: GPoint, nextPoint: GPoint, tiledLayer: Layer) -> None:
        graphics.drawLine(nextPoint.getX() - tiledLayer.getXP(), nextPoint.getY() - tiledLayer.getYP(), point.getX() - tiledLayer.getXP(), point.getY() - tiledLayer.getYP())
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.layer.Layer import Layer


LinePathRelativeAnimation.instanceC = LinePathRelativeAnimation()

