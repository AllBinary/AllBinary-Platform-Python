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

import time
from org.allbinary.canvas.AndroidGameStatistics import AndroidGameStatistics


class ProfilingRefreshHelper(AndroidGameStatistics):
    instance: ProfilingRefreshHelper = None

    def _init_fields(self) -> None:
        self.firstTime: bool = True
        self.bestFrameProcessingTime: int = 0
        self.worstFrameProcessingTime: int = 0
        self.frameProcessingTimeElapsed: int = 0
    

    @staticmethod
    def getInstance() -> AndroidGameStatistics:
        return ProfilingRefreshHelper.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def initView(self, view: View) -> None:
        super().initView(view)
        self.frameProcessingTimeElapsed = self.getTimeDelayHelper().getStartTime()
        self.bestFrameProcessingTime = 2147483647
        self.worstFrameProcessingTime = 0
    

    def nextFrame(self) -> None:
        self.frameProcessingTimeElapsed = int(time.time() * 1000) - self.frameProcessingTimeElapsed
        if self.firstTime != True:
            if self.frameProcessingTimeElapsed > self.worstFrameProcessingTime:
                self.worstFrameProcessingTime = self.frameProcessingTimeElapsed
            if self.frameProcessingTimeElapsed < self.bestFrameProcessingTime:
                self.bestFrameProcessingTime = self.frameProcessingTimeElapsed
        else:
            self.firstTime = False
        super().nextFrame()
    

    def toString(self) -> str:
        return str(StringMaker().append(str(super())).append(" Worst: ").appendint(self.worstFrameProcessingTime).append(" Best: ").appendint(self.bestFrameProcessingTime))

    def __str__(self) -> str:
        return self.toString()
from android.view.View import View
from org.allbinary.logic.string.StringMaker import StringMaker


ProfilingRefreshHelper.instance = ProfilingRefreshHelper()

