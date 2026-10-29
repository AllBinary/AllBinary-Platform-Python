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
# package org.allbinary.media.image.comparison.motion

from __future__ import annotations

from org.allbinary.media.image.comparison.motion.MotionRectangles import MotionRectangles


class ConsolidateMotionRectangles(MotionRectangles):
    NAME: str = "consolidatedMotionRectangles_"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, motionRectangles: MotionRectangles) -> None:
        super().__init__(ConsolidateMotionRectangles.NAME, motionRectangles.getImageComparisonResult())
        self._init_fields()
        vector: BasicArrayList = motionRectangles.getVector()
        size: int = vector.size()
        for index in range(0, size):
            motionRectangle: MotionRectangle = vector.get(index)
            vector.add(motionRectangle.clone())
        self.consolidateMotionRectangles()
    

    def consolidateMotionRectangles(self) -> None:
        vector: BasicArrayList = self.getVector()
        self.logUtil.putF("Start - Size Before: " + str(vector.size()), self, "consolidateMotionRectangleConstraints")
        removeVector: BasicArrayList = BasicArrayListD()
        size: int = vector.size()
        for index in range(0, size):
            motionRectangle: MotionRectangle = vector.get(index)
            for i in range(index + 1, vector.size()):
                motionRectangle2: MotionRectangle = vector.get(i)
                rectangle: Rectangle = motionRectangle.getRectangle()
                rectangle2: Rectangle = motionRectangle2.getRectangle()
                x2: int = rectangle.x + rectangle.width
                y2: int = rectangle.y + rectangle.height
                rightX: int = rectangle2.x + rectangle2.width
                bottomY: int = rectangle2.y + rectangle2.height
                if rectangle.x <= rectangle2.x and rectangle.y <= rectangle2.y and x2 >= rightX and y2 >= bottomY:
                    removeVector.add(motionRectangle2)
        self.remove(removeVector)
    

    def remove(self, removeVector: BasicArrayList) -> None:
        vector: BasicArrayList = self.getVector()
        size: int = removeVector.size()
        for index in range(0, size):
            vector.remove(removeVector.get(index))
# from java.awt import *
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


