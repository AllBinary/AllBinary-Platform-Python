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
# package org.allbinary.math

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FrameUtil:
    instance: FrameUtil = None
    

    @staticmethod
    def getInstance() -> FrameUtil:
        from jsinterop.annotations.JsMethod import JsMethod
        return FrameUtil.instance
    

    def __init__(self) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        pass
    

    def getFrameForAngle(self, angle: int, angleIncrement: int) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        return int(self.adjustAngleToFrameAngle(angle) / angleIncrement)
    

    def getFrameAngle(self, frame: int, angleIncrement: int) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        frameAngle: int = angleIncrement * frame - 90
        return self.adjustAngleToFrameAngle(frameAngle)
    

    def adjustAngleToFrameAngle(self, currentAngle: int) -> int:
        from org.allbinary.math.AngleFactory import AngleFactory
        from jsinterop.annotations.JsMethod import JsMethod
        angleFactory: AngleFactory = AngleFactory.getInstance()
        if currentAngle > 359:
            currentAngle = (currentAngle - angleFactory.TOTAL_ANGLE)
            while currentAngle > 359:
                currentAngle = (currentAngle - angleFactory.TOTAL_ANGLE)
        if currentAngle < 0:
            currentAngle = (currentAngle + angleFactory.TOTAL_ANGLE)
            while currentAngle < 0:
                currentAngle = (currentAngle + angleFactory.TOTAL_ANGLE)
        return currentAngle
# from jsinterop.annotations.JsType import JsType
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor


def _FrameUtil_instance() -> object:
    return FrameUtil()

lazy_static(FrameUtil, "instance", _FrameUtil_instance)

