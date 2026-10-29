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
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.game.identification.GroupInterfaceCompositeInterface import GroupInterfaceCompositeInterface
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.layer.NamedInterface import NamedInterface
from org.allbinary.layer.PositionInterface import PositionInterface


# Java interface
class LayerInterface(NamedInterface, PaintableInterface, GroupInterfaceCompositeInterface, PositionInterface):
    

    def getHeight(self) -> int:
        raise NotImplementedError()
    

    def getWidth(self) -> int:
        raise NotImplementedError()
    

    def getHalfHeight(self) -> int:
        raise NotImplementedError()
    

    def getHalfWidth(self) -> int:
        raise NotImplementedError()
    

    def getXP(self) -> int:
        raise NotImplementedError()
    

    def getYP(self) -> int:
        raise NotImplementedError()
    

    def getZP(self) -> int:
        raise NotImplementedError()
    

    def getX2(self) -> int:
        raise NotImplementedError()
    

    def getY2(self) -> int:
        raise NotImplementedError()
    

    def getZ2(self) -> int:
        raise NotImplementedError()
    

    def isVisible(self) -> bool:
        raise NotImplementedError()
    

    def moveDXYZ(self, dx: int, dy: int, dz: int) -> None:
        raise NotImplementedError()
    

    def setVisible(self, visible: bool) -> None:
        raise NotImplementedError()
    

    def implmentsTickableInterface(self) -> bool:
        raise NotImplementedError()
    

    def implmentsCollidableInterface(self) -> bool:
        raise NotImplementedError()
    

    def implmentsGameInputInterface(self) -> bool:
        raise NotImplementedError()
    

    def implmentsArtificialIntelligenceCompositeInterface(self) -> bool:
        raise NotImplementedError()
    

    def getType(self) -> int:
        raise NotImplementedError()


