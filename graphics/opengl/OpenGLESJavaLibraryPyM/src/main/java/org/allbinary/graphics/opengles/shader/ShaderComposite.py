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



class ShaderComposite:

    def _init_fields(self) -> None:
        self.disableProgramShaderOpenGLProcessor: OpenGLProcessor = None
        self.requiresOpenGLVersion: str = None
        self.shaderArray: list[Shader] = None
        self.shaderInitializer: ShaderInitializer = None
        self.compositeShaderUpdater: CompositeShaderUpdater = None
        self.modelViewProjection: ModelViewProjection = None
        self.colorOpenGLProcessor: OpenGLProcessor = None
        self.vertexOpenGLProcessor: OpenGLProcessor = None
        self.useProgramShaderOpenGLProcessor: OpenGLProcessor = None
        self.shaderMatrixOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.colorEnableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.normalEnableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.vertexEnableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.textureEnableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.colorDisableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.normalDisableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.vertexDisableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.textureDisableVertexAttribArrayOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.uniformLightPositionOpenGLProcessor: OpenGLObject3dProcessor = NullOpenGLTextureProcessor.getInstance()
        self.uniformLightColorOpenGLProcessor: OpenGLObject3dProcessor = NullOpenGLTextureProcessor.getInstance()
        self.uniformCameraPositionOpenGLProcessor: OpenGLObject3dProcessor = NullOpenGLTextureProcessor.getInstance()
        self.uniformTextureUnitOpenGLProcessor: OpenGLObject3dProcessor = NullOpenGLTextureProcessor.getInstance()
        self.programHandle: int = 0
    

    def __init__(self, requiresOpenGLVersion: str, shaderArray: list[Shader], compositeShaderUpdater: CompositeShaderUpdater, shaderInitializer: ShaderInitializer, modelViewProjection: ModelViewProjection, colorOpenGLProcessor: OpenGLProcessor, vertexOpenGLProcessor: OpenGLProcessor, disableProgramShaderOpenGLProcessor: OpenGLProcessor) -> None:
        self._init_fields()
        self.requiresOpenGLVersion = requiresOpenGLVersion
        self.shaderArray = shaderArray
        self.shaderInitializer = shaderInitializer
        self.compositeShaderUpdater = compositeShaderUpdater
        self.modelViewProjection = modelViewProjection
        self.colorOpenGLProcessor = colorOpenGLProcessor
        self.vertexOpenGLProcessor = vertexOpenGLProcessor
        self.disableProgramShaderOpenGLProcessor = disableProgramShaderOpenGLProcessor
    

    def init(self, gl: GL10) -> None:
        self.programHandle = self.shaderInitializer.init(gl, self.shaderArray, self.compositeShaderUpdater.attributeArray)
# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.graphics.opengles.OpenGLProcessor import OpenGLProcessor
from org.allbinary.graphics.opengles.NullOpenGLProcessorFactory import NullOpenGLProcessorFactory
from org.allbinary.graphics.opengles.shader.NullOpenGLTextureProcessor import NullOpenGLTextureProcessor


