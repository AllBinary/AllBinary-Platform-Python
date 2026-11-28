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
# package org.allbinary.graphics.threed

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


#SWTWithoutJOGL
class SWTJOGLProcessor(object):
    instance: SWTJOGLProcessor = None

    def _init_fields(self) -> None:
        _java_listener_owner = self
        class _JavaListenerN65771(GLHolder):
                


            def run(self, renderer: object) -> None:
                pass
        self.glHolder: GLHolder = _JavaListenerN65771()
            

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> SWTJOGLProcessor:
        return SWTJOGLProcessor.instance
    

    def init(self, display: object, comp: object) -> None:
        pass
    

    def isHolderCreated(self) -> bool:
        return self.glHolder.isCreated
    

    def setRenderer(self, renderer: object) -> None:
        pass
    

    def isJOGL(self) -> bool:
        return False
    

    def createSurface(self) -> None:
        pass
    

    def onSurfaceCreated(self) -> None:
        pass
    

    def onSurfaceChangedForEvent(self, event: object) -> None:
        pass
    

    def onSurfaceChanged(self) -> None:
        pass
    

    def onSurfaceChangedWH(self, width: int, height: int) -> None:
        pass
    

    def addListener(self) -> None:
        pass
    

    def addListeners(self, midlet: MIDlet) -> None:
        from javax.microedition.midlet.MIDlet import MIDlet
        pass
    

    def run(self) -> None:
        pass
    

    def clear(self) -> None:
        pass
    

    def setCustom(self, width: int, height: int, ratio: float) -> None:
        pass
    

    def setRatioProcessor(self, ratioProcessor: RatioProcessor) -> None:
        pass
    

    def charWidth(self, font: Font, ch: str) -> int:
        from javax.microedition.lcdui.Font import Font
        raise RuntimeError()
    

    def charsWidth(self, font: Font, ch: list[str], offset: int, length: int) -> int:
        from javax.microedition.lcdui.Font import Font
        raise RuntimeError()
    

    def stringWidth(self, font: Font, str_: str) -> int:
        from javax.microedition.lcdui.Font import Font
        raise RuntimeError()
    

    def substringWidth(self, font: Font, str_: str, offset: int, len_: int) -> int:
        from javax.microedition.lcdui.Font import Font
        raise RuntimeError()
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.midlet.MIDlet import MIDlet
from org.allbinary.graphics.threed.GLHolder import GLHolder


def _SWTJOGLProcessor_instance() -> object:
    return SWTJOGLProcessor()

lazy_static(SWTJOGLProcessor, "instance", _SWTJOGLProcessor_instance)

