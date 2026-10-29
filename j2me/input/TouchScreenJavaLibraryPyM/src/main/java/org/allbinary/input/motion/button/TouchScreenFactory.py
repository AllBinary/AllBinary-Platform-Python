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
# package org.allbinary.input.motion.button

from __future__ import annotations



class TouchScreenFactory:
    SINGLETON: TouchScreenFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.touch: bool = False
        self.multiTouch: bool = False
        self.multiTouchDistinct: bool = False
        self.touchScreenType: TouchScreenType = TouchScreenTypesFactory.getInstance().NOTOUCH
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            self.setTouch(True)
            self.setMultiTouch(False)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, TouchScreenFactory.SINGLETON, commonStrings.GET_INSTANCE, e)
    

    @staticmethod
    def getInstance() -> TouchScreenFactory:
        return TouchScreenFactory.SINGLETON
    

    def setMultiTouch(self, multiTouch: bool) -> None:
        self.multiTouch = multiTouch
    

    def isMultiTouch(self) -> bool:
        return self.multiTouch
    

    def setTouch(self, touch: bool) -> None:
        self.touch = touch
    

    def isTouch(self) -> bool:
        return self.touch
    

    def setMultiTouchDistinct(self, multiTouchDistinct: bool) -> None:
        self.multiTouchDistinct = multiTouchDistinct
    

    def isMultiTouchDistinct(self) -> bool:
        return self.multiTouchDistinct
    

    def setTouchScreenType(self, touchScreenType: TouchScreenType) -> None:
        self.touchScreenType = touchScreenType
    

    def getTouchScreenType(self) -> TouchScreenType:
        return self.touchScreenType
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("TouchScreen: ")
        stringBuffer.appendboolean(self.isTouch())
        stringBuffer.append(" MultiTouch: ")
        stringBuffer.appendboolean(self.isMultiTouch())
        stringBuffer.append(" Distinct MultiTouch: ")
        stringBuffer.appendboolean(self.isMultiTouchDistinct())
        stringBuffer.append(" TouchScreenType: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.getTouchScreenType()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.input.motion.button.TouchScreenTypesFactory import TouchScreenTypesFactory


TouchScreenFactory.SINGLETON = TouchScreenFactory()

