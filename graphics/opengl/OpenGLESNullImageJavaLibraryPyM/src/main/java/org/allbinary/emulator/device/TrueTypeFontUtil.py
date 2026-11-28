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
# package org.allbinary.emulator.device

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.emulator.device.TrueTypeFontUtilBase import TrueTypeFontUtilBase


@java_inherited_overloads
class TrueTypeFontUtil(TrueTypeFontUtilBase):
    instance: TrueTypeFontUtil = None
    def _java_defaults(self):
        vars(self).setdefault("fontImage", None)

    def _init_fields(self) -> None:
        from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
        self.fontImage: OpenGLESImage = OpenGLESImage.NULL_OPENGL_IMAGE
    

    @staticmethod
    def getInstance() -> TrueTypeFontUtil:
        return TrueTypeFontUtil.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__(1)
        __class__._init_fields(self)
    

    def getAsTextureSize(self, textureSize: int) -> int:
        raise RuntimeError()
    

    def getCellSize(self, cellSize: int) -> int:
        raise RuntimeError()
    

    def getFontBitmap(self, filename: str, fontSize: int, cellSize: int, basicColor: BasicColor) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        raise RuntimeError()
    

    def saveFontAtlasAsFile(self) -> None:
        pass
    

    def getFontBitmapGL(self, gl: GL10, filename: str, cellSize: int, basicColor: BasicColor) -> Image:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        raise RuntimeError()
    

    def getFontWidths(self, filename: str, fontSize: int) -> list[int]:
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


def _TrueTypeFontUtil_instance() -> object:
    return TrueTypeFontUtil()

lazy_static(TrueTypeFontUtil, "instance", _TrueTypeFontUtil_instance)

