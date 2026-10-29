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

from org.allbinary.graphics.opengles.shader.ShaderComposite import ShaderComposite


class PlatformShaderComposite(ShaderComposite):
    

    def __init__(self, requiresOpenGLVersion: str, shaderArray: list[Shader], compositeShaderUpdater: CompositeShaderUpdater, shaderInitializer: ShaderInitializer, modelViewProjection: ModelViewProjection, colorOpenGLProcessor: OpenGLProcessor, vertexOpenGLProcessor: OpenGLProcessor) -> None:
        super().__init__(requiresOpenGLVersion, shaderArray, compositeShaderUpdater, shaderInitializer, modelViewProjection, colorOpenGLProcessor, vertexOpenGLProcessor, NullOpenGLProcessorFactory.getInstance())
from org.allbinary.graphics.opengles.NullOpenGLProcessorFactory import NullOpenGLProcessorFactory
from org.allbinary.graphics.opengles.OpenGLProcessor import OpenGLProcessor


