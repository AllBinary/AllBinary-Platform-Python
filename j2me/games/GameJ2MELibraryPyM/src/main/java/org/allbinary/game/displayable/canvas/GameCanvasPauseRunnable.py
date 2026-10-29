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


class GameCanvasPauseRunnable(GameRunnable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.allBinaryGameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.allBinaryGameCanvas = allBinaryGameCanvas
    

    def run(self) -> None:
        pass
    

    # throws Exception
    def processLoopSleep(self) -> None:
        try:
            features: Features = Features.getInstance()
            isOpenGL: bool = features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL)
            if isOpenGL:
                self.allBinaryGameCanvas.processSleep()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


