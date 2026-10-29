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



#OpenGLNone
class SWTJOGLProcessor(object):
    instance: SWTJOGLProcessor = None
    

    @staticmethod
    def getInstance() -> SWTJOGLProcessor:
        return SWTJOGLProcessor.instance
    

    def init(self, display: object, comp: object) -> None:
        pass
    

    def isHolderCreated(self) -> bool:
        return True
    

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
        pass
    

    def run(self) -> None:
        pass
    

    def clear(self) -> None:
        pass
    

    def setCustom(self, width: int, height: int, ratio: float) -> None:
        pass
    

    def setRatioProcessor(self, ratioProcessor: RatioProcessor) -> None:
        pass
    

    def isPortraitRatioProcessor(self) -> bool:
        return True
    

    def charWidth(self, font: Font, ch: str) -> int:
        raise RuntimeError()
    

    def charsWidth(self, font: Font, ch: list[str], offset: int, length: int) -> int:
        raise RuntimeError()
    

    def stringWidth(self, font: Font, str_: str) -> int:
        raise RuntimeError()
    

    def substringWidth(self, font: Font, str_: str, offset: int, len_: int) -> int:
        raise RuntimeError()
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.midlet.MIDlet import MIDlet


SWTJOGLProcessor.instance = SWTJOGLProcessor()

