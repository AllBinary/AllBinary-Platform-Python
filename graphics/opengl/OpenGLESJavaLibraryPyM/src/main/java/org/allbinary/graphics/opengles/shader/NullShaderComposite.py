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

# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.graphics.opengles.NullOpenGLProcessorFactory import NullOpenGLProcessorFactory
from org.allbinary.graphics.opengles.OpenGLCapabilities import OpenGLCapabilities
from org.allbinary.graphics.opengles.shader.ShaderComposite import ShaderComposite
from org.allbinary.graphics.opengles.shader.Shader import Shader
from org.allbinary.graphics.opengles.shader.CompositeShaderUpdater import CompositeShaderUpdater
from org.allbinary.graphics.opengles.shader.ShaderInitializer import ShaderInitializer
from org.allbinary.graphics.opengles.shader.ModelViewProjection import ModelViewProjection


class NullShaderComposite(ShaderComposite):
    instance: NullShaderComposite = None
    

    @staticmethod
    def getInstance() -> ShaderComposite:
        return NullShaderComposite.instance
    

    def __init__(self, requiresOpenGLVersion: str, shaderArray: list[Shader], compositeShaderUpdater: CompositeShaderUpdater, shaderInitializer: ShaderInitializer, modelViewProjection: ModelViewProjection, colorOpenGLProcessor: OpenGLProcessor, vertexOpenGLProcessor: OpenGLProcessor, disableProgramShaderOpenGLProcessor: OpenGLProcessor) -> None:
        super().__init__(requiresOpenGLVersion, shaderArray, compositeShaderUpdater, shaderInitializer, modelViewProjection, colorOpenGLProcessor, vertexOpenGLProcessor, disableProgramShaderOpenGLProcessor)
        self.useProgramShaderOpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
from org.allbinary.graphics.opengles.OpenGLProcessor import OpenGLProcessor


NullShaderComposite.instance = (NullShaderComposite(OpenGLCapabilities.getInstance().VERSION_2_0, [Shader(), Shader()], CompositeShaderUpdater.getInstance(), ShaderInitializer.getInstance(), ModelViewProjection.getInstance(), None, None, NullOpenGLProcessorFactory.getInstance())  # Java anonymous class body:
#         
# 
#         def init(self, gl: GL10) -> None:
#             pass
)

