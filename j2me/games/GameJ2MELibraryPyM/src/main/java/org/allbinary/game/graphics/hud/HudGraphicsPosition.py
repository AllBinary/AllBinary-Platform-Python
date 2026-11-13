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

from java.lang.JavaRuntimeStatic import lazy_static


class HudGraphicsPosition:
    NULL_HUD_GRAPHICS_POSITION: HudGraphicsPosition = None

    def _init_fields(self) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.PointFactory import PointFactory
        self.anchor: int = 0
        self.point: GPoint = PointFactory.getInstance().ZERO_ZERO
    

    def __init__(self, point: GPoint, anchor: int) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        self._init_fields()
        self.setAnchor(anchor)
        self.setPoint(point)
    

    def getAnchor(self) -> int:
        return self.anchor
    

    def setAnchor(self, anchor: int) -> None:
        self.anchor = anchor
    

    def getPoint(self) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        return self.point
    

    def setPoint(self, point: GPoint) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        self.point = point
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.PointFactory import PointFactory


def _HudGraphicsPosition_NULL_HUD_GRAPHICS_POSITION() -> object:
    from org.allbinary.graphics.PointFactory import PointFactory
    return HudGraphicsPosition(PointFactory.getInstance().ZERO_ZERO, 9)

lazy_static(HudGraphicsPosition, "NULL_HUD_GRAPHICS_POSITION", _HudGraphicsPosition_NULL_HUD_GRAPHICS_POSITION)

