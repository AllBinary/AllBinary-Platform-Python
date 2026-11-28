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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


#Many devices don't support this even though it is supposed to
@java_inherited_overloads
class OpenGLESGL11ExtImage(OpenGLESImage):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("a", 0)
        vars(self).setdefault("rectangle", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "a" not in vars(self): self.a: int = 0
        if "rectangle" not in vars(self): self.rectangle: list[int] = None
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
        from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
        super().__init__(image, bitmapFactory, textureFactory)
        __class__._init_fields(self)
        self.onDisplayChangeEvent(DisplayInfoSingleton.getInstance().displayChangeEvent)
        self.rectangle = [0, self.getHeight(), self.getWidth(), -self.getHeight()]
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onResize")
            self.a = DisplayInfoSingleton.getInstance().getLastHeight() - self.getHeight()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onResize", e)
    

    def set(self, gl: GL) -> None:
        from javax.microedition.khronos.opengles.GL import GL
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.khronos.opengles.GL11 import GL11
        from javax.microedition.khronos.opengles.GL11Ext import GL11Ext
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
        self.onDisplayChangeEvent(DisplayInfoSingleton.getInstance().displayChangeEvent)
        gl11: GL11 = gl
        if java_super_call(super(), "initTexture", gl11):
            self.textureFactory.load(gl11, GL10.GL_TEXTURE_2D, 0, self, 0, True)
            gl11.glTexParameteriv(GL10.GL_TEXTURE_2D, GL11Ext.GL_TEXTURE_CROP_RECT_OES, self.rectangle, 0)
            gl11.glDisable(GL10.GL_TEXTURE_2D)
            OpenGLLogUtil.getInstance().logError(gl11, self)
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.khronos.opengles.GL11Ext import GL11Ext
        gl.glEnable(GL10.GL_TEXTURE_2D)
        gl.glBindTexture(GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
        gl11Ext: GL11Ext = gl
        gl11Ext.glDrawTexfOES(float(x), float((self.a - y)), float(z), float(self.getWidth()), float(self.getHeight()))
        gl.glDisable(GL10.GL_TEXTURE_2D)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.khronos.opengles.GL11 import GL11
# from javax.microedition.khronos.opengles.GL11Ext import GL11Ext
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
# from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
# from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory


