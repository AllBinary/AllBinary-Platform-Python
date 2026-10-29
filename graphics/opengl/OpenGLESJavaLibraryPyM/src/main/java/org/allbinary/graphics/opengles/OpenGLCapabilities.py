#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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
# package org.allbinary.graphics.opengles

from __future__ import annotations



class OpenGLCapabilities:
    instance: OpenGLCapabilities = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.CUSTOM_GL_SURFACE_VIEW: bool = True
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.initialized: bool = False
        self.glVersionString: str = self.stringUtil.EMPTY_STRING
        self.glShaderVersionString: str = self.stringUtil.EMPTY_STRING
        self.shaderVersion: int = 0
        self.glRenderer: str = self.stringUtil.EMPTY_STRING
        self.glVendor: str = self.stringUtil.EMPTY_STRING
        self.glExtensions: str = self.stringUtil.EMPTY_STRING
        self.possiblyAccelerated: bool = False
        self.acceleratedString: str = self.stringUtil.EMPTY_STRING
        self.maxTextureSize: int = 64
        self.VERSION_1_0: str = "1.0"
        self.VERSION_1_1: str = "1.1"
        self.VERSION_2_0: str = "2.0"
        self.VERSION_3_0: str = "3.0"
        self.VERSION_3_1: str = "3.1"
        self.VERSION_3_2: str = "3.2"
        self.VERSION_HIGHER_THAN_EXISTS: str = "999.999"
        self.VERSION_UNK: str = "Unk"
        self.GL_EXT_GPU_SHADER_100: str = "GL_ARB_shading_language_100"
        self.GL_EXT_GPU_SHADER4: str = "GL_EXT_gpu_shader4"
        self.glVersion: str = self.glVersionString
        self.glInstanceVersion: str = self.VERSION_UNK
        self.glExtensionDrawTexture: bool = False
        self.glThreedDrawTexture: bool = False
        self.glExtensionGPUShader4: bool = False
        self.glExtensionGPUShader100: bool = False
        self.vertexBufferObjectSupport: bool = False
    

    @staticmethod
    def getInstance() -> OpenGLCapabilities:
        return OpenGLCapabilities.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def isInitialized(self) -> bool:
        return self.initialized
    

    def requireInitialization(self) -> None:
        pass
    

    def initCapabilities(self, gl: GL10) -> None:
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        METHOD_NAME: str = "initGLCapabilities"
        try:
            features: Features = Features.getInstance()
            openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
            openGLImageSpecificFactory: OpenGLImageSpecificFactory = OpenGLImageSpecificFactory.getInstance()
            stringBuffer: StringMaker = StringMaker()
            self.glVersionString = gl.glGetString(self.GL10.GL_VERSION)
            GL_SHADING_LANGUAGE_VERSION: int = 0x8b8c
            self.glShaderVersionString = gl.glGetString(GL_SHADING_LANGUAGE_VERSION)
            if self.glShaderVersionString is None:
                self.glShaderVersionString = self.stringUtil.EMPTY_STRING
            try:
                if self.glShaderVersionString is not None and self.glShaderVersionString.find('.') >= 0:
                    startIndex: int = self.glShaderVersionString.rfind(' ')
                    if startIndex >= 0:
                        self.glShaderVersionString = self.glShaderVersionString[startIndex + 1:]
                    self.shaderVersion = int(self.glShaderVersionString.replace(CommonSeps.getInstance().PERIOD, StringUtil.getInstance().EMPTY_STRING))
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, METHOD_NAME, e)
            self.glRenderer = gl.glGetString(self.GL10.GL_RENDERER)
            self.glVendor = gl.glGetString(self.GL10.GL_VENDOR)
            self.glExtensions = gl.glGetString(self.GL10.GL_EXTENSIONS)
            if self.glExtensions.find(self.GL_EXT_GPU_SHADER_100) >= 0:
                self.glExtensionGPUShader100 = True
            else:
                self.glExtensionGPUShader100 = False
            if self.glExtensions.find(self.GL_EXT_GPU_SHADER4) >= 0:
                self.glExtensionGPUShader4 = True
            else:
                self.glExtensionGPUShader4 = False
            if self.glRenderer is None:
                self.glRenderer = self.stringUtil.EMPTY_STRING
            if self.glRenderer.lower().find("pixelflinger") >= 0:
                self.acceleratedString = "Probably Not for " + self.glRenderer
                self.possiblyAccelerated = False
            else:
                self.acceleratedString = "Probably for " + self.glRenderer
                self.possiblyAccelerated = True
            self.glExtensionDrawTexture = False
            if self.glVersionString is None:
                self.glVersionString = self.stringUtil.EMPTY_STRING
                self.glVersion = self.VERSION_UNK
            elif self.glVersionString.find(" 1.0") >= 0:
                self.glVersion = self.VERSION_1_0
            elif self.glVersionString.find(" 1.1") >= 0:
                self.glVersion = self.VERSION_1_1
            else:
                self.glVersion = self.VERSION_UNK
            if isinstance(gl, GL11):
                self.glInstanceVersion = self.VERSION_1_1
            elif isinstance(gl, GL10):
                self.glInstanceVersion = self.VERSION_1_0
            if self.glVendor is None:
                self.glVendor = self.stringUtil.EMPTY_STRING
            if self.glExtensions is None:
                self.glExtensions = self.stringUtil.EMPTY_STRING
            if self.possiblyAccelerated:
                PreLogUtil.put(str(StringMaker().append("VBO:?").appendboolean((self.glInstanceVersion == self.VERSION_1_1)).append("||").appendboolean(self.isExtension(openGLFeatureFactory.OPENGL_VERTEX_BUFFER_OBJECT))), self, METHOD_NAME)
                if (self.glInstanceVersion == self.VERSION_1_1 or self.isExtension(openGLFeatureFactory.OPENGL_VERTEX_BUFFER_OBJECT)):
                    if AndroidUtil.isAndroid():
                        PreLogUtil.put("VBO implementation was detected, but disabled by default for Android", self, METHOD_NAME)
                    else:
                        PreLogUtil.put("VBO implementation was detected, but disabled for now", self, METHOD_NAME)
            stringUtil: StringUtil = StringUtil.getInstance()
            if features.isDefault(openGLFeatureFactory.OPENGL_AUTO_SELECT):
                if self.vertexBufferObjectSupport:
                    openGLImageSpecificFactory.setImageFactory(OpenGLESGL11VBOImageFactory())
                else:
                    stringBuffer.append("OpenGL is on but ")
                    stringBuffer.append(stringUtil.toString(openGLFeatureFactory.OPENGL_DRAW_TEXTURE))
                    stringBuffer.append(" was not available")
                    PreLogUtil.put(str(stringBuffer), self, METHOD_NAME)
                    openGLImageSpecificFactory.setImageFactory(OpenGLESGL10ImageFactory())
            else:
                stringBuffer.append(stringUtil.toString(openGLFeatureFactory.OPENGL_AUTO_SELECT))
                stringBuffer.append(" is not on")
                PreLogUtil.put(str(stringBuffer), self, METHOD_NAME)
                openGLImageSpecificFactory.setImageFactory(OpenGLESGL10ImageFactory())
            maxTextureSizeArray: list[int] = [0] * (1)
            gl.glGetIntegerv(self.GL10.GL_MAX_TEXTURE_SIZE, maxTextureSizeArray, 0)
            self.maxTextureSize = maxTextureSizeArray[0]
            self.initialized = True
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, METHOD_NAME, e)
    

    def isExtension(self, gameFeature: OpenGLFeature) -> bool:
        index: int = self.glExtensions.find(gameFeature.getName())
        if index >= 0:
            return True
        else:
            return False
    

    def isGlExtensionDrawTexture(self) -> bool:
        self.requireInitialization()
        return self.glExtensionDrawTexture
    

    def isGlExtensionGPUShader100(self) -> bool:
        return self.glExtensionGPUShader100
    

    def isGlExtensionGPUShader4(self) -> bool:
        self.requireInitialization()
        return self.glExtensionGPUShader4
    

    def getGlVersion(self) -> str:
        self.requireInitialization()
        return self.glVersion
    

    def getGlVersionString(self) -> str:
        self.requireInitialization()
        return self.glVersionString
    

    def getGlShaderVersion(self) -> str:
        self.requireInitialization()
        return self.glShaderVersionString
    

    def isGlThreedDrawTexture(self) -> bool:
        self.requireInitialization()
        return self.glThreedDrawTexture
    

    def getGlRenderer(self) -> str:
        self.requireInitialization()
        return self.glRenderer
    

    def isVertexBufferObjectSupport(self) -> bool:
        self.requireInitialization()
        return self.vertexBufferObjectSupport
    

    def isTextureSizeValid(self, widthAndHeight: int) -> bool:
        self.requireInitialization()
        if self.maxTextureSize >= widthAndHeight:
            return True
        return False
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("GL_VERSION: ")
        stringBuffer.append(self.glVersionString)
        stringBuffer.append(" GL_SHADING_LANGUAGE_VERSION: ")
        stringBuffer.append(self.glShaderVersionString)
        stringBuffer.append(" GL_RENDERER: ")
        stringBuffer.append(self.glRenderer)
        stringBuffer.append(" GL_VENDOR: ")
        stringBuffer.append(self.glVendor)
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(" Is Accelerated: ")
        stringBuffer.append(self.acceleratedString)
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(" VBO Support: ")
        stringBuffer.appendboolean(self.isVertexBufferObjectSupport())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(" Max Texture Size: ")
        stringBuffer.appendint(self.maxTextureSize)
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(" GL_EXTENSIONS: ")
        try:
            tokenizer: Tokenizer = Tokenizer(commonSeps.SPACE)
            list_: BasicArrayList = tokenizer.getTokensFromString(self.glExtensions, BasicArrayListD())
            size: int = list_.size()
            for index in range(0, size):
                stringBuffer.append(commonSeps.NEW_LINE)
                stringBuffer.append(self.stringUtil.toString(list_.objectArray[index]))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, commonStrings.TOSTRING, e)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.khronos.opengles.GL11 import GL11
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.image.opengles.OpenGLESGL10ImageFactory import OpenGLESGL10ImageFactory
from org.allbinary.image.opengles.OpenGLESGL11VBOImageFactory import OpenGLESGL11VBOImageFactory
from org.allbinary.image.opengles.OpenGLImageSpecificFactory import OpenGLImageSpecificFactory
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.logic.communication.log.LogUtil import LogUtil


OpenGLCapabilities.instance = OpenGLCapabilities()

