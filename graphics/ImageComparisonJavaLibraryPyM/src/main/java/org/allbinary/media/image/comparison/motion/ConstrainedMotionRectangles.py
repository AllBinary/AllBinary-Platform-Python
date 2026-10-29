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


class ConstrainedMotionRectangles(MotionRectangles):
    NAME: str = "constrainedMotionRectangles_"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface = None
    

    def __init__(self, motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface, motionRectangles: MotionRectangles) -> None:
        super().__init__(ConstrainedMotionRectangles.NAME, motionRectangles.getImageComparisonResult())
        self._init_fields()
        self.setMotionRectangleConstraintsInterface(motionRectangleConstraintsInterface)
    

    # throws Exception
    def applyMotionRectangleConstraints(self, motionRectangles: MotionRectangles) -> None:
        self.logUtil.putF("Start - Size Before: " + str(motionRectangles.getVector().size()), self, "applyMotionRectangleConstraints")
        bufferedImageArray: list[BufferedImage] = motionRectangles.getImageComparisonResult().getBufferedImages()
        bufferedImage: BufferedImage = bufferedImageArray[1]
        vector: BasicArrayList = BasicArrayListD()
        vector2: BasicArrayList = motionRectangles.getVector()
        size: int = vector2.size()
        for index in range(0, size):
            motionRectangle: MotionRectangle = vector2.get(index)
            rectangle: Rectangle = motionRectangle.getRectangle()
            isTooSmall: bool = self.getMotionRectangleConstraintsInterface().isTooSmall(rectangle)
            if isTooSmall:
                continue
            isAreaTooSmall: bool = self.getMotionRectangleConstraintsInterface().isAreaTooSmall(rectangle)
            if isAreaTooSmall:
                continue
            isTooBig: bool = self.getMotionRectangleConstraintsInterface().isTooBig(rectangle)
            if isTooBig:
                continue
            isValid: bool = self.getMotionRectangleConstraintsInterface().isValid(self.getImageComparisonResult().getFrameTwo(), bufferedImage, motionRectangle.getRectangle())
            if not isValid:
                continue
            if not isTooSmall and not isAreaTooSmall and not isTooBig and isValid:
                vector.add(motionRectangle)
        self.setVector(vector)
    

    def getMotionRectangleConstraintsInterface(self) -> MotionRectangleConstraintsInterface:
        return self.motionRectangleConstraintsInterface
    

    def setMotionRectangleConstraintsInterface(self, motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface) -> None:
        self.motionRectangleConstraintsInterface = motionRectangleConstraintsInterface
# from java.awt.Rectangle import Rectangle
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


