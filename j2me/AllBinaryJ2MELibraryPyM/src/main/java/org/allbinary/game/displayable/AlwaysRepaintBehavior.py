# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.displayable

from __future__ import annotations

import threading
from org.allbinary.game.displayable.RepaintBehavior import RepaintBehavior


class AlwaysRepaintBehavior(RepaintBehavior):
    instanceC: AlwaysRepaintBehavior = None

    def _init_fields(self) -> None:
        self.NAME: str = "AlwaysRepaintBehavior"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AlwaysRepaintBehavior:
        return AlwaysRepaintBehavior.instanceC
    

    def repaint(self, canvas: Canvas) -> None:
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        if features.isFeature(openGLFeatureFactory.OPENGL):
            DisplayInfoSingleton.getInstance().process()
        else:
            thread: threading.Thread = threading.Thread(target=(ARunnable()  # Java anonymous class body:
#                 
# 
#                 def run(self) -> None:
#                     try:
#                         canvas.repaint()
#                         DisplayInfoSingleton.getInstance().process()
#                     except Exception as e:
#                         commonStrings: CommonStrings = CommonStrings.getInstance()
#                         logUtil: LogUtil = LogUtil.getInstance()
#                         logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
).run, name=self.NAME)
            thread.start()
    

    def onChangeRepaint(self, canvas: Canvas) -> None:
        pass
from org.allbinary.thread.ARunnable import ARunnable
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.NullRunnable import NullRunnable


AlwaysRepaintBehavior.instanceC = AlwaysRepaintBehavior()

