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
# package org.allbinary.graphics.opengles.shader

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ShaderUpdater:
    instance: ShaderUpdater = None

    def _init_fields(self) -> None:
        from org.allbinary.graphics.opengles.renderer.RendererStrings import RendererStrings
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.rendererStrings: RendererStrings = RendererStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ShaderUpdater:
        return ShaderUpdater.instance
    

    def onSurfaceCreated(self, gl: GL10, eglConfig: EGLConfig) -> None:
        from javax.microedition.khronos.egl.EGLConfig import EGLConfig
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
# from javax.microedition.khronos.egl.EGLConfig import EGLConfig
# from javax.microedition.khronos.opengles.GL10 import GL10
# from org.allbinary.graphics.opengles.renderer.RendererStrings import RendererStrings
# from org.allbinary.string.CommonStrings import CommonStrings


def _ShaderUpdater_instance() -> object:
    return ShaderUpdater()

lazy_static(ShaderUpdater, "instance", _ShaderUpdater_instance)

