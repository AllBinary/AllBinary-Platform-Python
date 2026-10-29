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

from org.allbinary.canvas.BaseGameStatistics import BaseGameStatistics


class AndroidGameStatistics(BaseGameStatistics):

    def _init_fields(self) -> None:
        self.view: BaseViewWrapper = BaseViewWrapper.NULL_VIEW_WRAPPER
        self.totalOnDraws: int = 0
        self.ANDROID_STRING_ARRAY: list[str] = [None] * (14)
        self.TOTAL_ONDRAWS: str = " Total onDraws: "
        self.ONDRAWS_RATE: str = " onDraws(/10) Sec: "
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        stringUtil: StringUtil = StringUtil.getInstance()
        for index in range(0, len(self.ANDROID_STRING_ARRAY)):
            self.ANDROID_STRING_ARRAY[index] = stringUtil.EMPTY_STRING
    

    def initView(self, view: View) -> None:
        super().init()
        self.view = ViewWrapper(view)
        self.totalOnDraws = 0
    

    def process(self) -> None:
        self.view.postInvalidate()
    

    def nextOnDraw(self) -> None:
        self.totalOnDraws += 1
    

    def toStringArray(self) -> list[str]:
        stringArray: list[str] = super().toStringArray()
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
        totalTime: int = self.getTimeDelayHelper().getElapsed(self.gameTickTimeDelayHelper.startTime)
        totalTime = (int(totalTime / 1000))
        if totalTime > 0:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(super().toStringAt(totalTime))
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
from android.view.View import View
from org.allbinary.android.view.BaseViewWrapper import BaseViewWrapper
from org.allbinary.android.view.ViewWrapper import ViewWrapper
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


