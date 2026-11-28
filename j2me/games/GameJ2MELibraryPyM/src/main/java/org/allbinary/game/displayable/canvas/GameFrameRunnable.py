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
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.displayable.canvas.GameRunnable import GameRunnable


@java_inherited_overloads
class GameFrameRunnable(GameRunnable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("gameTickDisplayInfoSingleton", None)
        vars(self).setdefault("allBinaryGameCanvas", None)
        vars(self).setdefault("gameTickTimeDelayHelper", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.displayable.GameTickDisplayInfoSingleton import GameTickDisplayInfoSingleton
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameTickDisplayInfoSingleton: GameTickDisplayInfoSingleton = GameTickDisplayInfoSingleton.getInstance()
        if "allBinaryGameCanvas" not in vars(self): self.allBinaryGameCanvas: AllBinaryGameCanvas = None
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
    

    def __init__(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.allBinaryGameCanvas = allBinaryGameCanvas
    

    def run(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            allBinaryGameCanvas: AllBinaryGameCanvas = self.allBinaryGameCanvas
            allBinaryGameCanvas.getLoopTimeHelperP().setStartTime(self.gameTickTimeDelayHelper.setStartTime())
            self.gameTickDisplayInfoSingleton.update()
            allBinaryGameCanvas.processGame()
            if not (java_predicate(allBinaryGameCanvas, "isRunning")) or java_predicate(allBinaryGameCanvas, "isPaused"):
                allBinaryGameCanvas.notifyDonePainting()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
# from org.allbinary.graphics.displayable.GameTickDisplayInfoSingleton import GameTickDisplayInfoSingleton
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory


