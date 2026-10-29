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
# package org.allbinary.image.opengles

from __future__ import annotations



class OpenGLESImageProcessor:
    instance: OpenGLESImageProcessor = None
    

    @staticmethod
    def getInstance() -> OpenGLESImageProcessor:
        return OpenGLESImageProcessor.instance
    

    def translate(self, gl: GL10, translateX: float, translateY: float) -> None:
        pass
    

    def rotate(self, gl: GL10, angle: float) -> None:
        pass
    

    def scale(self, gl: GL10, scaleX: float, scaleY: float) -> None:
        pass
    

    def colorMask(self, gl: GL10, red: float, green: float, blue: float, alpha: float) -> None:
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10


OpenGLESImageProcessor.instance = OpenGLESImageProcessor()

