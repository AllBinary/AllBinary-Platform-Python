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

from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.graphics.PointFactory import PointFactory


class RelativeRelationship:
    NULL_RELATIVE_RELATIONSHIP: RelativeRelationship = None

    def _init_fields(self) -> None:
        self.typesAllowedList: BasicArrayList = None
        self.x: int = None
        self.y: int = None
        self.z: int = None
    

    def __init__(self, point: GPoint, typesAllowedList: BasicArrayList) -> None:
        self._init_fields()
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
        return self.typesAllowedList
    

    def setTypesAllowedList(self, typesAllowedList: BasicArrayList) -> None:
        self.typesAllowedList = typesAllowedList
from org.allbinary.util.BasicArrayList import BasicArrayList


RelativeRelationship.NULL_RELATIVE_RELATIONSHIP = RelativeRelationship(PointFactory.getInstance().ZERO_ZERO, BasicArrayListUtil.getInstance().getImmutableInstance())

