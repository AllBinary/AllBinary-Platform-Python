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
# package org.allbinary.media.graphics.geography.map.racetrack

from __future__ import annotations



class RaceTracksPathPrinter:
    

    def printPath(self, list_: BasicArrayList) -> None:
        size: int = list_.size()
        for index in range(0, size):
            anyType: object = list_.get(index)
            PreLogUtil.put(str(StringMaker().append("pathList.add(cellPositionFactory.getInstance").append(str(anyType)).append(");")), self, "printPath")
    

    def printPaths(self, list_: BasicArrayList) -> None:
        size: int = list_.size()
        for index in range(0, size):
            print(str(StringMaker().append(" Path ").appendint(index).append(CommonLabels.getInstance().COLON_SEP)))
            self.printPath(list_.get(index))
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonLabels import CommonLabels


