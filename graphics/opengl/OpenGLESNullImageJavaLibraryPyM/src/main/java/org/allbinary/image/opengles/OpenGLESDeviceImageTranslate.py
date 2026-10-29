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

from org.allbinary.image.opengles.OpenGLESImageTranslate import OpenGLESImageTranslate


class OpenGLESDeviceImageTranslate(OpenGLESImageTranslate):

    def _init_fields(self) -> None:
        self.translateX: float = 0.0
        self.translateY: float = 0.0
        self.translateX2: float = 0.0
        self.translateY2: float = 0.0

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def translate(self, gl: GL10, openGLESImage: OpenGLESImage, x: float, y: float) -> None:
        openGLESImage.imageProcessor.translate(gl, self.translateX + (openGLESImage.openGLESImageProperties.scaleX * x), self.translateY + (openGLESImage.openGLESImageProperties.scaleY * y))
    

    def translate2(self, gl: GL10, openGLESImage: OpenGLESImage) -> None:
        openGLESImage.imageProcessor.translate(gl, self.translateX2, self.translateY2)
# from javax.microedition.khronos.opengles.GL10 import GL10


