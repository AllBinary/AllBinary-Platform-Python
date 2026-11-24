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
# package org.allbinary.game.score.displayable

from __future__ import annotations

import time
from org.allbinary.thread.ARunnable import ARunnable


class HighScoreRunnable(ARunnable):

    def _init_fields(self) -> None:
        self.highScoresCanvas: HighScoresCanvas = None
    

    def __init__(self, highScoresCanvas: HighScoresCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.highScoresCanvas = highScoresCanvas
    

    def run(self) -> None:
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonStrings import CommonStrings
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil: LogUtil = LogUtil.getInstance()
        highScoresCanvas: HighScoresCanvas = self.highScoresCanvas
        try:
            isHTML: bool = J2MEUtil.isHTML()
            if not isHTML:
                while not highScoresCanvas.hasPainted:
                    pass
                highScoresCanvas.hasPainted = False
            stringMaker: StringMaker = StringMaker()
            systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
            currentTimeMillis: int = systemWrapper.currentTimeMillis()
            logUtil.putF(str(stringMaker.append("HighScoresCanvas - Request repaint to be sure: ").appendlong(currentTimeMillis)), self, commonStrings.RUN)
            highScoresCanvas.repaintBehavior.onChangeRepaint(highScoresCanvas)
            if not isHTML:
                while not highScoresCanvas.hasPainted:
                    pass
            stringMaker.delete(0, stringMaker.length())
            logUtil.putF(str(stringMaker.append("HighScoresCanvas - Now that the canvas has completed repaint go ahead and fetch the scores: ").appendlong(currentTimeMillis)), self, commonStrings.RUN)
            highScoresCanvas.executeUpdate()
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
# from org.allbinary.J2MEUtil import J2MEUtil
# from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonStrings import CommonStrings


