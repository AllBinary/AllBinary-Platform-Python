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



class OpenGLESImageTranslate:
    instance: OpenGLESImageTranslate = None
    

    @staticmethod
    def getInstance() -> OpenGLESImageTranslate:
        return OpenGLESImageTranslate.instance
    

    def translate(self, gl: GL10, openGLESImage: OpenGLESImage, x: float, y: float) -> None:
        pass
    

    def translate2(self, gl: GL10, openGLESImage: OpenGLESImage) -> None:
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10


OpenGLESImageTranslate.instance = OpenGLESImageTranslate()

