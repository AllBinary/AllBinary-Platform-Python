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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static


class TouchScreenFactory:
    SINGLETON: TouchScreenFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "touch" not in vars(self): self.touch: bool = False
        if "multiTouch" not in vars(self): self.multiTouch: bool = False
        if "multiTouchDistinct" not in vars(self): self.multiTouchDistinct: bool = False
        self.touchScreenType: TouchScreenType = TouchScreenTypesFactory.getInstance().NOTOUCH
    

    def __init__(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        __class__._init_fields(self)
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
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("TouchScreen: ")
        stringBuffer.appendboolean(java_predicate(self, "isTouch"))
        stringBuffer.append(" MultiTouch: ")
        stringBuffer.appendboolean(java_predicate(self, "isMultiTouch"))
        stringBuffer.append(" Distinct MultiTouch: ")
        stringBuffer.appendboolean(java_predicate(self, "isMultiTouchDistinct"))
        stringBuffer.append(" TouchScreenType: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.getTouchScreenType()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.input.motion.button.TouchScreenTypesFactory import TouchScreenTypesFactory


def _TouchScreenFactory_SINGLETON() -> object:
    return TouchScreenFactory()

lazy_static(TouchScreenFactory, "SINGLETON", _TouchScreenFactory_SINGLETON)

