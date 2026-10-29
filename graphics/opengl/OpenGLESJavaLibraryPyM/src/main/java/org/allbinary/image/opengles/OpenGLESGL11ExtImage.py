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
# package org.allbinary.image.opengles

from __future__ import annotations

from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


#Many devices don't support this even though it is supposed to
class OpenGLESGL11ExtImage(OpenGLESImage):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.a: int = 0
        self.rectangle: list[int] = None
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        super().__init__(image, bitmapFactory, textureFactory)
        self._init_fields()
        self.onDisplayChangeEvent(None)
        self.rectangle = [0, self.getHeight(), self.getWidth(), -self.getHeight()]
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onResize")
            self.a = DisplayInfoSingleton.getInstance().getLastHeight() - self.getHeight()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onResize", e)
    

    def set(self, gl: GL) -> None:
        self.onDisplayChangeEvent(None)
        gl11: GL11 = gl
        if super().initTexture(gl11):
            self.textureFactory.load(gl11, self.GL10.GL_TEXTURE_2D, 0, self, 0, True)
            gl11.glTexParameteriv(self.GL10.GL_TEXTURE_2D, GL11Ext.GL_TEXTURE_CROP_RECT_OES, self.rectangle, 0)
            gl11.glDisable(self.GL10.GL_TEXTURE_2D)
            OpenGLLogUtil.getInstance().logError(gl11, self)
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        gl.glEnable(self.GL10.GL_TEXTURE_2D)
        gl.glBindTexture(self.GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
        (gl).glDrawTexfOES(x, self.a - y, z, self.getWidth(), self.getHeight())
        gl.glDisable(self.GL10.GL_TEXTURE_2D)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.khronos.opengles.GL11 import GL11
# from javax.microedition.khronos.opengles.GL11Ext import GL11Ext
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory


