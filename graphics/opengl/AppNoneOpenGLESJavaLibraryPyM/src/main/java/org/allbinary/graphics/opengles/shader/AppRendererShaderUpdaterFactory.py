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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.opengles.shader.ShaderUpdater import ShaderUpdater


@java_inherited_overloads
class AppRendererShaderUpdaterFactory(ShaderUpdater):
    instanceC: AppRendererShaderUpdaterFactory = None
    def _java_defaults(self):
        vars(self).setdefault("NULL_SHADER_COMPOSITE_ARRAY", None)
        vars(self).setdefault("shaderCompositeArray", None)
        vars(self).setdefault("shaderOpenGLProcessorArray", None)

    def _init_fields(self) -> None:
        self.NULL_SHADER_COMPOSITE_ARRAY: list[ShaderComposite] = [None] * (0)
        self.shaderCompositeArray: list[ShaderComposite] = self.NULL_SHADER_COMPOSITE_ARRAY
        self.shaderOpenGLProcessorArray: list[ShaderOpenGLProcessor] = [None] * (0)

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AppRendererShaderUpdaterFactory:
        return AppRendererShaderUpdaterFactory.instanceC
    

    def getTestShaders(self) -> list[ShaderOpenGLProcessor]:
        return self.shaderOpenGLProcessorArray
    

    def setShaderComposite(self, object3d: object) -> None:
        pass


def _AppRendererShaderUpdaterFactory_instanceC() -> object:
    return AppRendererShaderUpdaterFactory()

lazy_static(AppRendererShaderUpdaterFactory, "instanceC", _AppRendererShaderUpdaterFactory_instanceC)

