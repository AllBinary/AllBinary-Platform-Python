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
from org.allbinary.game.displayable.canvas.GameRunnable import GameRunnable


@java_inherited_overloads
class GameCanvasPauseRunnable(GameRunnable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("allBinaryGameCanvas", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "allBinaryGameCanvas" not in vars(self): self.allBinaryGameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.allBinaryGameCanvas = allBinaryGameCanvas
    

    def run(self) -> None:
        pass
    

    # throws Exception
    def processLoopSleep(self) -> None:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            features: Features = Features.getInstance()
            isOpenGL: bool = features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL)
            if isOpenGL:
                self.allBinaryGameCanvas.processSleep()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
# from org.allbinary.AndroidUtil import AndroidUtil
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


