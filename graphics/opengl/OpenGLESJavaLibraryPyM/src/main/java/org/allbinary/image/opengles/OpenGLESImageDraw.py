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

from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLESImageDraw:
    instance: OpenGLESImageDraw = None
    

    @staticmethod
    def getInstance() -> OpenGLESImageDraw:
        return OpenGLESImageDraw.instance
    

    def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10


def _OpenGLESImageDraw_instance() -> object:
    return OpenGLESImageDraw()

lazy_static(OpenGLESImageDraw, "instance", _OpenGLESImageDraw_instance)

