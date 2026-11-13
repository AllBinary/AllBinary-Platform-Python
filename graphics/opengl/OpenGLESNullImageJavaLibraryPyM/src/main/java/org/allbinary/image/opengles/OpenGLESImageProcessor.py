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


class OpenGLESImageProcessor:
    instance: OpenGLESImageProcessor = None
    

    @staticmethod
    def getInstance() -> OpenGLESImageProcessor:
        return OpenGLESImageProcessor.instance
    

    def translate(self, gl: GL10, translateX: float, translateY: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def rotate(self, gl: GL10, angle: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def scale(self, gl: GL10, scaleX: float, scaleY: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def colorMask(self, gl: GL10, red: float, green: float, blue: float, alpha: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10


def _OpenGLESImageProcessor_instance() -> object:
    return OpenGLESImageProcessor()

lazy_static(OpenGLESImageProcessor, "instance", _OpenGLESImageProcessor_instance)

