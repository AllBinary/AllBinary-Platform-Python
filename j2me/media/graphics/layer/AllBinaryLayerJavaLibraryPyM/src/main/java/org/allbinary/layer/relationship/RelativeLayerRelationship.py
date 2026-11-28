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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship


@java_inherited_overloads
class RelativeLayerRelationship(RelativeRelationship):
    def _java_defaults(self):
        vars(self).setdefault("layer", None)

    def _init_fields(self) -> None:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        self.layer: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
    

    def __init__(self, layer: AllBinaryLayer, point: GPoint, typesAllowedList: BasicArrayList) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(point, typesAllowedList)
        __class__._init_fields(self)
        self.layer = layer
    

    def getX(self) -> int:
        return self.layer.getXP() + java_super_call(super(), "getX")
    

    def getY(self) -> int:
        return self.layer.getYP() + java_super_call(super(), "getY")
    

    def getZ(self) -> int:
        return self.layer.getZP() + java_super_call(super(), "getZ")
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.util.BasicArrayList import BasicArrayList


