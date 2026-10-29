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



class AngleInfo:
    ANGLE: str = "Angle: "

    def _init_fields(self) -> None:
        self.angleIncrementInfo: AngleIncrementInfo = None
        self.angle: int = 0
        self.frameUtil: FrameUtil = FrameUtil.getInstance()
    

    @staticmethod
    def getInstance(angleIncrement: int) -> AngleInfo:
        from org.allbinary.math.AngleIncrementInfoFactory import AngleIncrementInfoFactory
        return AngleInfo(AngleIncrementInfoFactory.getInstance().getAt(angleIncrement))
    

    def __init__(self, angleIncrementInfo: AngleIncrementInfo) -> None:
        self._init_fields()
        self.angleIncrementInfo = angleIncrementInfo
    

    def adjustAngle(self, frame: int) -> None:
        newAngle: int = self.angleIncrementInfo.getAngleIncrement() * frame - 90
        self.setAngle(((int(self.frameUtil.adjustAngleToFrameAngle(newAngle)) + 32768) % 65536 - 32768))
    

    def getAngle(self) -> int:
        return self.angle
    

    def setAngle(self, angle: int) -> None:
        self.angle = angle
    

    def getAngleIncrementInfo(self) -> AngleIncrementInfo:
        return self.angleIncrementInfo
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(AngleInfo.ANGLE)
        stringBuffer.appendshort(self.angle)
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(StringUtil.getInstance().toString(self.getAngleIncrementInfo()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from org.allbinary.math.FrameUtil import FrameUtil


