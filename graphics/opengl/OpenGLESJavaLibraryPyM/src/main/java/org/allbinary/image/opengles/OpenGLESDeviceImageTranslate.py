# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.image.opengles.OpenGLESImageTranslate import OpenGLESImageTranslate


@java_inherited_overloads
class OpenGLESDeviceImageTranslate(OpenGLESImageTranslate):
    def _java_defaults(self):
        vars(self).setdefault("translateX", 0.0)
        vars(self).setdefault("translateY", 0.0)
        vars(self).setdefault("translateX2", 0.0)
        vars(self).setdefault("translateY2", 0.0)

    def _init_fields(self) -> None:
        self.translateX: float = 0.0
        self.translateY: float = 0.0
        self.translateX2: float = 0.0
        self.translateY2: float = 0.0

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def translate(self, gl: GL10, openGLESImage: OpenGLESImage, x: float, y: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        openGLESImage.imageProcessor.translate(gl, self.translateX + (openGLESImage.openGLESImageProperties.scaleX * x), self.translateY + (openGLESImage.openGLESImageProperties.scaleY * y))
    

    def translate2(self, gl: GL10, openGLESImage: OpenGLESImage) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        openGLESImage.imageProcessor.translate(gl, self.translateX2, self.translateY2)
# from javax.microedition.khronos.opengles.GL10 import GL10


