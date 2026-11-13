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

from java.lang.JavaRuntimeStatic import lazy_static


class FullScreenUtil:
    instance: FullScreenUtil = None
    

    @staticmethod
    def getInstance() -> FullScreenUtil:
        return FullScreenUtil.instance
    

    # throws Exception
    def initOnRun(self, fullScreenInterface: Canvas, commandListener: CommandListener) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from javax.microedition.lcdui.CommandListener import CommandListener
        if commandListener is not None:
            self.init(fullScreenInterface)
    

    def init(self, fullScreenInterface: Canvas) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        pass
    

    def isScreenChange(self, isFullScreen: bool) -> bool:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
        mainFeatureFactory: MainFeatureFactory = MainFeatureFactory.getInstance()
        features: Features = Features.getInstance()
        if features.isFeature(mainFeatureFactory.FULL_SCREEN) != isFullScreen:
            return True
        return False
    

    def isScreenChangeCanvas(self, fullScreenInterface: Canvas) -> bool:
        from javax.microedition.lcdui.Canvas import Canvas
        return self.isScreenChange(False)
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.CommandListener import CommandListener
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory


def _FullScreenUtil_instance() -> object:
    return FullScreenUtil()

lazy_static(FullScreenUtil, "instance", _FullScreenUtil_instance)

