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
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class RelativeRelationship:
    NULL_RELATIVE_RELATIONSHIP: RelativeRelationship = None

    def _init_fields(self) -> None:
        if "typesAllowedList" not in vars(self): self.typesAllowedList: BasicArrayList = None
        if "x" not in vars(self): self.x: int = 0
        if "y" not in vars(self): self.y: int = 0
        if "z" not in vars(self): self.z: int = 0
    

    def __init__(self, point: GPoint, typesAllowedList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        __class__._init_fields(self)
        self.x = point.getX()
        self.y = point.getY()
        self.z = point.getZ()
        self.typesAllowedList = typesAllowedList
    

    def getX(self) -> int:
        return self.x
    

    def getY(self) -> int:
        return self.y
    

    def getZ(self) -> int:
        return self.z
    

    def getTypesAllowedList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.typesAllowedList
    

    def setTypesAllowedList(self, typesAllowedList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.typesAllowedList = typesAllowedList
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


def _RelativeRelationship_NULL_RELATIVE_RELATIONSHIP() -> object:
    from org.allbinary.graphics.PointFactory import PointFactory
    from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
    return RelativeRelationship(PointFactory.getInstance().ZERO_ZERO, BasicArrayListUtil.getInstance().getImmutableInstance())

lazy_static(RelativeRelationship, "NULL_RELATIVE_RELATIONSHIP", _RelativeRelationship_NULL_RELATIVE_RELATIONSHIP)

