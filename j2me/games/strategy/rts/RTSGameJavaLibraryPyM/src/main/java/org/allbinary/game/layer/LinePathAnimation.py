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



class LinePathAnimation:
    instance: LinePathAnimation = None
    

    @staticmethod
    def getInstance() -> LinePathAnimation:
        return LinePathAnimation.instance
    

    def paint(self, graphics: Graphics, point: GPoint, nextPoint: GPoint, tiledLayer: Layer) -> None:
        graphics.drawLine(nextPoint.getX(), nextPoint.getY(), point.getX(), point.getY())
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.layer.Layer import Layer


LinePathAnimation.instance = LinePathAnimation()

