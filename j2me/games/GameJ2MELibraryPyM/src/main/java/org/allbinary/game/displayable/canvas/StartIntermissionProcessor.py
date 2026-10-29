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

from org.allbinary.canvas.Processor import Processor


class StartIntermissionProcessor(Processor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameCanvas: AllBinaryGameCanvas = None
        self.WAIT: int = 5000
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.gameCanvas = gameCanvas
    

    # throws Exception
    def process(self) -> None:
        if self.gameCanvas.getStartIntermissionInterface().getTimeDelayHelper().isElapsedTNT(self.WAIT):
            self.logUtil.putF("Intermission End", self, self.commonStrings.PROCESS)
            self.gameCanvas.getStartIntermissionInterface().setEnabled(False)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


