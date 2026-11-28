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
# package org.allbinary.input.automation.module

from __future__ import annotations

from org.allbinary.media.image.comparison.ImageComparatorConstraintsInterface import ImageComparatorConstraintsInterface


class ImageComparatorConstraints(ImageComparatorConstraintsInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "avoidVector" not in vars(self): self.avoidVector: BasicArrayList = None
        if "maxNonMatchingPixelDeltas" not in vars(self): self.maxNonMatchingPixelDeltas: int = 0
        if "doImageComparisonEveryNthFrame" not in vars(self): self.doImageComparisonEveryNthFrame: int = 0
    

    def __init__(self, doImageComparisonEveryNthFrame: int) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        __class__._init_fields(self)
        self.doImageComparisonEveryNthFrame = doImageComparisonEveryNthFrame
        self.setAvoidVector(BasicArrayListD())
    

    def getAvoidVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.avoidVector
    

    def isColorAllowed(self, frame: int, point: GPoint, color: Color) -> bool:
        from org.allbinary.graphics.GPoint import GPoint
        raise RuntimeError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def isCollisionWithAvoidRectangles_j1_1(self, rectangle: Rectangle) -> bool:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.collision.RectangleCollisionUtil import RectangleCollisionUtil
        isCollsionWithAvoidRectangles: bool = False
        avoidVector: BasicArrayList = self.getAvoidVector()
        size: int = avoidVector.size()
        for index in range(0, size):
            avoidRectangle: Rectangle = avoidVector.get(index)
            if RectangleCollisionUtil.isCollision(avoidRectangle, rectangle):
                isCollsionWithAvoidRectangles = True
        return isCollsionWithAvoidRectangles
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def isCollisionWithAvoidRectangles_j1_2(self, point: GPoint) -> bool:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.collision.RectangleCollisionUtil import RectangleCollisionUtil
        from org.allbinary.graphics.GPoint import GPoint
        isCollsionWithAvoidRectangles: bool = False
        avoidVector: BasicArrayList = self.getAvoidVector()
        size: int = avoidVector.size()
        for index in range(0, size):
            avoidRectangle: Rectangle = avoidVector.get(index)
            if RectangleCollisionUtil.isCollision(avoidRectangle, point):
                isCollsionWithAvoidRectangles = True
                break
        return isCollsionWithAvoidRectangles

    def isCollisionWithAvoidRectangles(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "Rectangle" for base in type(args[0]).__mro__)):
            return __class__.__dict__["isCollisionWithAvoidRectangles_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["isCollisionWithAvoidRectangles_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("isCollisionWithAvoidRectangles_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().isCollisionWithAvoidRectangles(*args)
    

    def setAvoidVector(self, avoidVector: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.avoidVector = avoidVector
    

    def getMaxNonMatchingPixelDeltas(self) -> int:
        return self.maxNonMatchingPixelDeltas
    

    def setMaxNonMatchingPixelDeltas(self, maxNonMatchingPixelDeltas: int) -> None:
        self.maxNonMatchingPixelDeltas = maxNonMatchingPixelDeltas
    

    def isFrameAllowed(self, frame: int) -> bool:
        remainder: int = ((frame + 1) % self.doImageComparisonEveryNthFrame)
        self.logUtil.putF(" Frame: " + str(frame) + " remainder: " + str(remainder) + " this.doImageComparisonEveryNthFrame: " + str(self.doImageComparisonEveryNthFrame), self, "isCollisionWithAvoidRectangles")
        if remainder == 0:
            return True
        else:
            return False
    

    # throws Exception
    def isImageValid(self, bufferedImage: BufferedImage) -> bool:
        raise RuntimeError()
    

    def log(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        avoidVector: BasicArrayList = self.getAvoidVector()
        size: int = avoidVector.size()
        for index in range(0, size):
            avoidRectangle: Rectangle = avoidVector.get(index)
            self.logUtil.putF("Avoid Rectangle: " + str(avoidRectangle), self, "log")
# from java.awt.Color import Color
# from java.awt.Rectangle import Rectangle
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.collision.RectangleCollisionUtil import RectangleCollisionUtil
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


