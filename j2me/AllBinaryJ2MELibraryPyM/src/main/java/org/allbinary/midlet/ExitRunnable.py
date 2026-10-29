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
# package org.allbinary.midlet

from __future__ import annotations



class ExitRunnable(object):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.midlet: AllBinaryMidlet = None
        self.processor: Processor = None
        self.isProgress: bool = None
    

    def __init__(self, midlet: AllBinaryMidlet, processor: Processor, isProgress: bool) -> None:
        self._init_fields()
        self.midlet = midlet
        self.isProgress = isProgress
        self.processor = processor
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START_RUNNABLE, self, self.commonStrings.RUN)
            self.midlet.destroyAppInRunnable(False, self.isProgress)
            self.midlet.setDisplay(NullCanvas.NULL_CANVAS)
            self.midlet.notifyDestroyed()
            self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
            self.processor.process()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
            try:
                self.processor.process()
            except Exception as e2:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from javax.microedition.lcdui.NullCanvas import NullCanvas
from org.allbinary.canvas.Processor import Processor
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


