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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.thread.ABRunnable import ABRunnable


@java_inherited_overloads
class DemoGameStartupRunnable(ABRunnable):
    TYPE: int = 4
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("demoCanvas", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "demoCanvas" not in vars(self): self.demoCanvas: DemoCanvas = None
    

    def __init__(self, demoCanvas: DemoCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.demoCanvas = demoCanvas
    

    def run(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            self.setRunning(True)
            self.demoCanvas.stopGameDemo()
            self.demoCanvas.create()
            self.demoCanvas.start()
            self.setRunning(False)
        except Exception as e:
            self.setRunning(False)
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    

    def getType(self) -> int:
        return DemoGameStartupRunnable.TYPE
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


