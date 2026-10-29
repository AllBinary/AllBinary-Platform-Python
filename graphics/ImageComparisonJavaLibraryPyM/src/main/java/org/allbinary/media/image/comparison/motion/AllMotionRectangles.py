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


class AllMotionRectangles(MotionRectangles):
    NAME: str = "allMotionRectangles_"
    

    def __init__(self, imageComparisonResult: ImageComparisonResult) -> None:
        super().__init__(AllMotionRectangles.NAME, imageComparisonResult)
        self.createMotionRectangles(imageComparisonResult)
    

    # throws Exception
    def createMotionRectangles(self, imageComparisonInfo: ImageComparisonResult) -> None:
        vector: BasicArrayList = imageComparisonInfo.getNonMatchingPixelVector()
        size: int = vector.size()
        for index in range(0, size):
            pixelDelta: PixelDelta = vector.get(index)
            self.addPixelDeltaToAMotionRectangle(pixelDelta)
    

    # throws Exception
    def addPixelDeltaToExistingMotionRectangle(self, pixelDelta: PixelDelta) -> bool:
        vector: BasicArrayList = self.getVector()
        size: int = vector.size()
        for index in range(0, size):
            motionRectangle: MotionRectangle = vector.get(index)
            if self.shouldPixelDeltaPartOfMotionRectangle(motionRectangle, pixelDelta):
                newWidth: int = pixelDelta.getPoint().getX() - motionRectangle.getRectangle().x
                newHeight: int = pixelDelta.getPoint().getY() - motionRectangle.getRectangle().y
                if newWidth < motionRectangle.getRectangle().width:
                    newWidth = motionRectangle.getRectangle().width
                if newHeight < motionRectangle.getRectangle().height:
                    newHeight = motionRectangle.getRectangle().height
                motionRectangle.getRectangle().setSize(newWidth, newHeight)
                return True
        return False
    

    # throws Exception
    def addPixelDeltaToAMotionRectangle(self, pixelDelta: PixelDelta) -> None:
        from org.allbinary.media.image.comparison.motion.Rectangle import Rectangle
        from org.allbinary.media.image.comparison.motion.MotionRectangle import MotionRectangle
        if not self.addPixelDeltaToExistingMotionRectangle(pixelDelta):
            newRectangle: Rectangle = Rectangle(pixelDelta.getPoint().getX(), pixelDelta.getPoint().getY(), 1, 1)
            motionRectangle: MotionRectangle = MotionRectangle(newRectangle)
            motionRectangle.getPixelDeltaVector().add(pixelDelta)
            self.getVector().add(motionRectangle)
    

    # throws Exception
    def shouldPixelDeltaPartOfMotionRectangle(self, motionRectangle: MotionRectangle, pixelDelta: PixelDelta) -> bool:
        isPixelLeftOfTheRectangle: bool = False
        if motionRectangle.getRectangle().y > pixelDelta.getPoint().getY():
            raise Exception("PixelAboveTheRectangle")
        if motionRectangle.getRectangle().x > pixelDelta.getPoint().getX():
            isPixelLeftOfTheRectangle = True
        if not isPixelLeftOfTheRectangle:
            return self.isPixelDeltaLikelyPartOfMotionRectangle(motionRectangle, pixelDelta)
        return False
    

    # throws Exception
    def isPixelDeltaLikelyPartOfMotionRectangle(self, motionRectangle: MotionRectangle, pixelDelta: PixelDelta) -> bool:
        maxX: int = motionRectangle.getRectangle().x + motionRectangle.getRectangle().width
        maxY: int = motionRectangle.getRectangle().y + motionRectangle.getRectangle().height
        horizontalDistance: int = pixelDelta.getPoint().getX() - maxX
        verticalDistance: int = pixelDelta.getPoint().getY() - maxY
        if horizontalDistance < self.MAX_PIXEL_DISTANCE_THRESHOLD and verticalDistance < self.MAX_PIXEL_DISTANCE_THRESHOLD:
            return True
        return False
# from java.awt import *
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult
from org.allbinary.media.image.comparison.pixel.PixelDelta import PixelDelta


