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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class InputFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.KEY_CODE_LABEL: str = "KeyCode: "
        self.DEVICE_ID_LABEL: str = "DeviceId: "
        self.MAX: int = SmallIntegerSingletonFactory.getInstance().getMin()
        self.inputIntegerArray: list[Input] = [None] * (self.MAX)
        self.NO_INPUT: Input = Input(0, self.commonStrings.UNKNOWN)
    

    @staticmethod
    def getInstance() -> InputFactory:
        if InputFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            InputFactory.instance = InputFactory()
        return InputFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
        size: int = len(self.inputIntegerArray)
        for index in range(0, size):
            self.inputIntegerArray[index] = self.NO_INPUT
    

    def add(self, id: int, input: Input) -> None:
        self.inputIntegerArray[id] = input
    

    def getInstanceById(self, id: int) -> Input:
        if id < 0:
            id = -id
        if id > len(self.inputIntegerArray):
            self.logUtil.putF(str(StringMaker().append("Warning id: ").appendint(id)), self, self.commonStrings.GET_INSTANCE)
            return self.NO_INPUT
        return self.inputIntegerArray[id]
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.input.Input import Input


