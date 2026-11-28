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
# package org.allbinary.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.canvas.BaseGameStatistics import BaseGameStatistics


@java_inherited_overloads
class AndroidGameStatistics(BaseGameStatistics):
    def _java_defaults(self):
        vars(self).setdefault("view", None)
        vars(self).setdefault("totalOnDraws", 0)
        vars(self).setdefault("ANDROID_STRING_ARRAY", None)
        vars(self).setdefault("TOTAL_ONDRAWS", None)
        vars(self).setdefault("ONDRAWS_RATE", None)

    def _init_fields(self) -> None:
        from org.allbinary.android.view.BaseViewWrapper import BaseViewWrapper
        self.view: BaseViewWrapper = BaseViewWrapper.NULL_VIEW_WRAPPER
        if "totalOnDraws" not in vars(self): self.totalOnDraws: int = 0
        self.ANDROID_STRING_ARRAY: list[str] = [None] * (14)
        self.TOTAL_ONDRAWS: str = " Total onDraws: "
        self.ONDRAWS_RATE: str = " onDraws(/10) Sec: "
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.string.StringUtil import StringUtil
        super().__init__()
        __class__._init_fields(self)
        stringUtil: StringUtil = StringUtil.getInstance()
        for index in range(0, len(self.ANDROID_STRING_ARRAY)):
            self.ANDROID_STRING_ARRAY[index] = stringUtil.EMPTY_STRING
    

    def initView(self, view: View) -> None:
        from android.view.View import View
        from org.allbinary.android.view.ViewWrapper import ViewWrapper
        java_super_call(super(), "init")
        self.view = ViewWrapper(view)
        self.totalOnDraws = 0
    

    def process(self) -> None:
        self.view.postInvalidate()
    

    def nextOnDraw(self) -> None:
        self.totalOnDraws += 1
    

    def toStringArray(self) -> list[str]:
        stringArray: list[str] = java_super_call(super(), "toStringArray")
        for index in range(0, len(stringArray)):
            self.ANDROID_STRING_ARRAY[index] = stringArray[index]
        totalTime: int = self.getTimeDelayHelper().getElapsed(self.gameTickTimeDelayHelper.startTime)
        totalTime = (int(totalTime / 10000))
        self.ANDROID_STRING_ARRAY[10] = self.TOTAL_ONDRAWS
        self.ANDROID_STRING_ARRAY[11] = str(self.totalOnDraws)
        self.ANDROID_STRING_ARRAY[12] = self.ONDRAWS_RATE
        self.ANDROID_STRING_ARRAY[13] = str(int(self.totalOnDraws / totalTime))
        return self.ANDROID_STRING_ARRAY
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        totalTime: int = self.getTimeDelayHelper().getElapsed(self.gameTickTimeDelayHelper.startTime)
        totalTime = (int(totalTime / 1000))
        if totalTime > 0:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(java_super_call(super(), "toStringAt", totalTime))
            if self.totalOnDraws > 0:
                stringBuffer.append(self.TOTAL_ONDRAWS)
                stringBuffer.append(str(self.totalOnDraws))
                stringBuffer.append(self.ONDRAWS_RATE)
                drawsOverTime: str = str(int(self.totalOnDraws / totalTime))
                stringBuffer.append(drawsOverTime)
            return str(stringBuffer)
        else:
            return self.NOT

    def __str__(self) -> str:
        return self.toString()
# from android.view.View import View
# from org.allbinary.android.view.BaseViewWrapper import BaseViewWrapper
# from org.allbinary.android.view.ViewWrapper import ViewWrapper
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil


