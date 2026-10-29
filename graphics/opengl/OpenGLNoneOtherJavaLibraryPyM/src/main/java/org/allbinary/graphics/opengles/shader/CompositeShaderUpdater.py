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

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.opengles.shader.ShaderUpdater import ShaderUpdater


class CompositeShaderUpdater(ShaderUpdater):
    instanceC: CompositeShaderUpdater = None

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
    

    @staticmethod
    def getInstance() -> CompositeShaderUpdater:
        return CompositeShaderUpdater.instanceC
    

    def __init__(self, uniformBlockArray: list[str], uniformArray: list[str], attributeArray: list[str], attributeHandleArray: list[int]) -> None:
        super().__init__()
        self._init_fields()
    

    def onSurfaceCreated(self, gl: GL10, eglConfig: EGLConfig, programHandle: int) -> None:
        pass
    

    def onSurfaceDestroyed(self, gl: GL10) -> None:
        pass
# from javax.microedition.khronos.egl.EGLConfig import EGLConfig
# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.string.CommonSeps import CommonSeps


CompositeShaderUpdater.instanceC = CompositeShaderUpdater(StringUtil.getInstance().getArrayInstance(), StringUtil.getInstance().getArrayInstance(), StringUtil.getInstance().getArrayInstance(), NullUtil.getInstance().NULL_INT_ARRAY)

