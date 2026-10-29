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

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class MotionRectanglesResultsEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.frame: int = None
        self.motionRectangles: MotionRectangles = None
    

    def __init__(self, anyType: object, frame: int, motionRectangles: MotionRectangles) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.frame = frame
        self.setMotionRectangles(motionRectangles)
    

    def getMotionRectangles(self) -> MotionRectangles:
        return self.motionRectangles
    

    def setMotionRectangles(self, motionRectangles: MotionRectangles) -> None:
        self.motionRectangles = motionRectangles
    

    def getFrame(self) -> int:
        return self.frame


