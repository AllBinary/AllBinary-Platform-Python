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

from org.allbinary.graphics.opengles.shader.ShaderUpdater import ShaderUpdater


class AppRendererShaderUpdaterFactory(ShaderUpdater):
    instanceC: AppRendererShaderUpdaterFactory = None

    def _init_fields(self) -> None:
        self.NULL_SHADER_COMPOSITE_ARRAY: list[ShaderComposite] = [None] * (0)
        self.shaderCompositeArray: list[ShaderComposite] = self.NULL_SHADER_COMPOSITE_ARRAY
        self.shaderOpenGLProcessorArray: list[ShaderOpenGLProcessor] = [None] * (0)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AppRendererShaderUpdaterFactory:
        return AppRendererShaderUpdaterFactory.instanceC
    

    def getTestShaders(self) -> list[ShaderOpenGLProcessor]:
        return self.shaderOpenGLProcessorArray
    

    def setShaderComposite(self, object3d: object) -> None:
        pass


AppRendererShaderUpdaterFactory.instanceC = AppRendererShaderUpdaterFactory()

