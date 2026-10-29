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
# package org.allbinary.game.layer

from __future__ import annotations



class GameLayerUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def isOnScreen(layer: AllBinaryLayer) -> bool:
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        viewPosition: ViewPositionBase = layer.getViewPosition()
        return GameLayerUtil.isInside(viewPosition.getX(), viewPosition.getY(), viewPosition.getX2(), viewPosition.getY2(), 0, 0, displayInfo.getLastWidth(), displayInfo.getLastHeight())
    

    @staticmethod
    def isInside(rectX1: int, rectY1: int, rectX2: int, rectY2: int, rect2X1: int, rect2Y1: int, rect2X2: int, rect2Y2: int) -> bool:
        if rectX1 > rect2X1 and rectX2 < rect2X2 and rectY1 > rect2Y1 and rectY2 < rect2Y2:
            return True
        else:
            return False
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.view.ViewPositionBase import ViewPositionBase


