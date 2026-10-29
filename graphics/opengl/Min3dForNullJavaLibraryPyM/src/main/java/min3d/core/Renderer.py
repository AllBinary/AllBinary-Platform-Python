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
# package min3d.core

from __future__ import annotations



# Java interface
class Renderer:
    

    def onSurfaceCreated(self, gl: GL10, config: EGLConfig) -> None:
        raise NotImplementedError()
    

    def onSurfaceChanged(self, gl: GL10, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def onDrawFrame(self, gl: GL10) -> None:
        raise NotImplementedError()
# from javax.microedition.khronos.egl.EGLConfig import EGLConfig
# from javax.microedition.khronos.opengles.GL10 import GL10


