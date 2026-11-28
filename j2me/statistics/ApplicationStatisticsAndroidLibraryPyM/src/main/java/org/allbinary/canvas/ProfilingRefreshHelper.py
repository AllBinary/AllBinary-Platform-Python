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
from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.canvas.AndroidGameStatistics import AndroidGameStatistics


@java_inherited_overloads
class ProfilingRefreshHelper(AndroidGameStatistics):
    instance: ProfilingRefreshHelper = None
    def _java_defaults(self):
        vars(self).setdefault("firstTime", False)
        vars(self).setdefault("bestFrameProcessingTime", 0)
        vars(self).setdefault("worstFrameProcessingTime", 0)
        vars(self).setdefault("frameProcessingTimeElapsed", 0)

    def _init_fields(self) -> None:
        self.firstTime: bool = True
        if "bestFrameProcessingTime" not in vars(self): self.bestFrameProcessingTime: int = 0
        if "worstFrameProcessingTime" not in vars(self): self.worstFrameProcessingTime: int = 0
        if "frameProcessingTimeElapsed" not in vars(self): self.frameProcessingTimeElapsed: int = 0
    

    @staticmethod
    def getInstance() -> AndroidGameStatistics:
        return ProfilingRefreshHelper.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def initView(self, view: View) -> None:
        from android.view.View import View
        java_super_call(super(), "initView", view)
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
        java_super_call(super(), "nextFrame")
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        return str(StringMaker().append(java_super_call(super(), "toString")).append(" Worst: ").appendint(self.worstFrameProcessingTime).append(" Best: ").appendint(self.bestFrameProcessingTime))

    def __str__(self) -> str:
        return self.toString()
# from android.view.View import View
# from org.allbinary.logic.string.StringMaker import StringMaker


def _ProfilingRefreshHelper_instance() -> object:
    return ProfilingRefreshHelper()

lazy_static(ProfilingRefreshHelper, "instance", _ProfilingRefreshHelper_instance)

