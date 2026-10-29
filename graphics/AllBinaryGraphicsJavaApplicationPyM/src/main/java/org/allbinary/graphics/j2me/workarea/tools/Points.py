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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations

from org.allbinary.graphics.j2me.workarea.tools.PointsInterface import PointsInterface


class Points(PointsInterface):

    def _init_fields(self) -> None:
        self.pointVector: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.pointVector = BasicArrayListD()
    

    def init(self) -> None:
        self.pointVector.clear()
    

    def getPoints(self) -> BasicArrayList:
        return self.pointVector
    

    def addPoints(self, vector: BasicArrayList) -> None:
        self.pointVector.addAll2(vector)
    

    def isValid(self) -> bool:
        if self.pointVector.size() > 1:
            return True
        else:
            return False
    

    def getSize(self) -> int:
        return self.pointVector.size()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


