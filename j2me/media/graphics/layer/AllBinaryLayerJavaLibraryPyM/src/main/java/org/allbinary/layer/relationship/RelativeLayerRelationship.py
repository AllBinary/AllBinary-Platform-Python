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
# package org.allbinary.layer.relationship

from __future__ import annotations

from org.allbinary.graphics.RelativeRelationship import RelativeRelationship


class RelativeLayerRelationship(RelativeRelationship):

    def _init_fields(self) -> None:
        self.layer: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
    

    def __init__(self, layer: AllBinaryLayer, point: GPoint, typesAllowedList: BasicArrayList) -> None:
        super().__init__(point, typesAllowedList)
        self._init_fields()
        self.layer = layer
    

    def getX(self) -> int:
        return self.layer.getXP() + super().getX()
    

    def getY(self) -> int:
        return self.layer.getYP() + super().getY()
    

    def getZ(self) -> int:
        return self.layer.getZP() + super().getZ()
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.util.BasicArrayList import BasicArrayList


