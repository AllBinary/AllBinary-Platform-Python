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
# package org.allbinary.game.graphics.hud

from __future__ import annotations

from org.allbinary.graphics.PointFactory import PointFactory


class HudGraphicsPosition:
    NULL_HUD_GRAPHICS_POSITION: HudGraphicsPosition = None

    def _init_fields(self) -> None:
        self.anchor: int = 0
        self.point: GPoint = PointFactory.getInstance().ZERO_ZERO
    

    def __init__(self, point: GPoint, anchor: int) -> None:
        self._init_fields()
        self.setAnchor(anchor)
        self.setPoint(point)
    

    def getAnchor(self) -> int:
        return self.anchor
    

    def setAnchor(self, anchor: int) -> None:
        self.anchor = anchor
    

    def getPoint(self) -> GPoint:
        return self.point
    

    def setPoint(self, point: GPoint) -> None:
        self.point = point
from org.allbinary.graphics.GPoint import GPoint


HudGraphicsPosition.NULL_HUD_GRAPHICS_POSITION = HudGraphicsPosition(PointFactory.getInstance().ZERO_ZERO, 9)

