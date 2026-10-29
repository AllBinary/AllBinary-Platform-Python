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

from org.allbinary.game.displayable.canvas.GameRunnable import GameRunnable


class RunnableCanvasSingleThreadStartRunnable(GameRunnable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.runnableCanvas: RunnableCanvas = None
    

    def __init__(self, demoCanvas: RunnableCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.runnableCanvas = demoCanvas
    

    def run(self) -> None:
        try:
            self.runnableCanvas.run()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    

    # throws Exception
    def processLoopSleep(self) -> None:
        self.runnableCanvas.processLoopSleep()
from org.allbinary.canvas.RunnableCanvas import RunnableCanvas
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


