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
# package org.allbinary.input

from __future__ import annotations

from org.allbinary.input.AllBinarySensorListener import AllBinarySensorListener


class AllBinarySensor(AllBinarySensorListener):
    NULL_ALLBINARY_SENSOR: AllBinarySensor = None
    max: int = 100

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        pass
    

    # throws Exception
    def update(self) -> None:
        pass
    

    @staticmethod
    def setMax(max: int) -> None:
        AllBinarySensor.max = max
    

    @staticmethod
    def getMax() -> int:
        return AllBinarySensor.max
    

    def getId(self) -> int:
        return AllBinarySensor.getMax()
    

    def shutdown(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "shutdown")
    

    def onSensorChange(self) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


AllBinarySensor.NULL_ALLBINARY_SENSOR = AllBinarySensor()

