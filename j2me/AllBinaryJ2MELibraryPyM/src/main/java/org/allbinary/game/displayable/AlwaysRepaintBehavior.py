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

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.displayable.RepaintBehavior import RepaintBehavior


@java_inherited_overloads
class AlwaysRepaintBehavior(RepaintBehavior):
    instanceC: AlwaysRepaintBehavior = None
    def _java_defaults(self):
        vars(self).setdefault("NAME", None)

    def _init_fields(self) -> None:
        self.NAME: str = "AlwaysRepaintBehavior"

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AlwaysRepaintBehavior:
        return AlwaysRepaintBehavior.instanceC
    

    def repaint(self, canvas: Canvas) -> None:
        from org.allbinary.game.displayable.RepaintRunnable import RepaintRunnable
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        if features.isFeature(openGLFeatureFactory.OPENGL):
            DisplayInfoSingleton.getInstance().process()
        else:
            thread: JavaThread = JavaThread(target=RepaintRunnable(canvas).run, name=self.NAME)
            thread.start()
    

    def onChangeRepaint(self, canvas: Canvas) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        pass
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.thread.NullRunnable import NullRunnable


def _AlwaysRepaintBehavior_instanceC() -> object:
    return AlwaysRepaintBehavior()

lazy_static(AlwaysRepaintBehavior, "instanceC", _AlwaysRepaintBehavior_instanceC)

