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



class AngleFactory:
    instance: AngleFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.TOTAL_ANGLE: int = 360
        self.QUARTER_TOTAL_ANGLE: int = 90
        self.angleArray: list[Angle] = [None] * (self.TOTAL_ANGLE)
        self.NEGATIVE_ONE: int = ((int(-1) + 32768) % 65536 - 32768)
        self.NOT_ANGLE: NamedAngle = NamedAngle(self.NEGATIVE_ONE, CommonStrings.getInstance().EMPTY)
        self.DOWN: NamedAngle = None
        self.UP: NamedAngle = None
        self.LEFT: NamedAngle = None
        self.RIGHT: NamedAngle = None
        self.frameUtil: FrameUtil = FrameUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AngleFactory:
        return AngleFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.math.NamedAngle import NamedAngle
        from org.allbinary.math.Angle import Angle
        from org.allbinary.math.NamedAngle import NamedAngle
        from org.allbinary.math.Angle import Angle
        from org.allbinary.math.NamedAngle import NamedAngle
        from org.allbinary.math.Angle import Angle
        from org.allbinary.math.NamedAngle import NamedAngle
        from org.allbinary.math.Angle import Angle
        self._init_fields()
        commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        total: int = ((int(len(self.angleArray)) + 32768) % 65536 - 32768)
        self.UP = NamedAngle(((int(0) + 32768) % 65536 - 32768), commonPhoneStrings.UP)
        self.angleArray[0] = self.UP
        for index in range(1, 90):
            self.angleArray[index] = Angle(((int(index) + 32768) % 65536 - 32768))
        self.RIGHT = NamedAngle(((int(90) + 32768) % 65536 - 32768), commonPhoneStrings.RIGHT)
        self.angleArray[90] = self.RIGHT
        for index in range(91, 180):
            self.angleArray[index] = Angle(((int(index) + 32768) % 65536 - 32768))
        self.DOWN = NamedAngle(((int(180) + 32768) % 65536 - 32768), commonPhoneStrings.DOWN)
        self.angleArray[180] = self.DOWN
        for index in range(181, 270):
            self.angleArray[index] = Angle(((int(index) + 32768) % 65536 - 32768))
        self.LEFT = NamedAngle(((int(270) + 32768) % 65536 - 32768), commonPhoneStrings.LEFT)
        self.angleArray[270] = self.LEFT
        for index in range(271, total):
            self.angleArray[index] = Angle(((int(index) + 32768) % 65536 - 32768))
    

    def getAt(self, index: int) -> Angle:
        adjustedIndex: int = int(self.frameUtil.adjustAngleToFrameAngle(index))
        return self.angleArray[adjustedIndex]
    

    def getClosestDirection(self, angle: int) -> Angle:
        if (angle >= 315 and angle < 360) or (angle >= 0 and angle < 45):
            return self.UP
        elif angle >= 45 and angle < 135:
            return self.RIGHT
        elif angle >= 135 and angle < 225:
            return self.DOWN
        elif angle >= 225 and angle < 315:
            return self.LEFT
        raise RuntimeError()
    

    def getGeneralDirection(self) -> Angle:
        return self.NOT_ANGLE
    

    @staticmethod
    def main(args: list[str]) -> None:
        stringMaker: StringMaker = StringMaker()
        angleFactory: AngleFactory = AngleFactory.getInstance()
        for index in range(0, 360):
            stringMaker.appendint(index).append(CommonSeps.getInstance().FORWARD_SLASH).appendshort(((int(angleFactory.getClosestDirection(index).getValue()) + 32768) % 65536 - 32768)).append(CommonSeps.getInstance().NEW_LINE)
        LogUtil.getInstance().putF(str(stringMaker), "main", "main")
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty
from org.allbinary.math.NamedAngle import NamedAngle
from org.allbinary.math.FrameUtil import FrameUtil


AngleFactory.instance = AngleFactory()

