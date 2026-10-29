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



class MotionRectangle(object):

    def _init_fields(self) -> None:
        self.rectangle: Rectangle = None
        self.pixelDeltaVector: BasicArrayList = None
    

    def __init__(self, rectangle: Rectangle) -> None:
        self._init_fields()
        self.setRectangle(rectangle)
        self.setPixelDeltaVector(BasicArrayListD())
    

    def getRectangle(self) -> Rectangle:
        return self.rectangle
    

    def setRectangle(self, rectangle: Rectangle) -> None:
        self.rectangle = rectangle
    

    def getPixelDeltaVector(self) -> BasicArrayList:
        return self.pixelDeltaVector
    

    def setPixelDeltaVector(self, pixelDeltaVector: BasicArrayList) -> None:
        self.pixelDeltaVector = pixelDeltaVector
    

    def clone(self) -> object:
        motionRectangle: MotionRectangle = MotionRectangle(self.getRectangle().clone())
        motionRectangle.setPixelDeltaVector(self.getPixelDeltaVector().clone())
        return motionRectangle
# from java.awt.Rectangle import Rectangle
# from java.util.Vector import Vector
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


