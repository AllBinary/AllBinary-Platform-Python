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
        self.VERSION_1_0: str = "1.0"
        self.VERSION_1_1: str = "1.1"
        self.VERSION_2_0: str = "2.0"
        self.VERSION_3_0: str = "3.0"
        self.VERSION_3_1: str = "3.1"
        self.VERSION_3_2: str = "3.2"
        self.VERSION_HIGHER_THAN_EXISTS: str = "999.999"
        self.glVersion: str = StringUtil.getInstance().EMPTY_STRING
        self.shaderVersion: int = 0
        self.glInstanceVersion: str = StringUtil.getInstance().EMPTY_STRING
        self.maxTextureSize: int = 64
    

    @staticmethod
    def getInstance() -> OpenGLCapabilities:
        return OpenGLCapabilities.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def initCapabilities(self, gl: object) -> None:
        pass
    

    def isGlExtensionDrawTexture(self) -> bool:
        return False
    

    def getGlVersion(self) -> str:
        return self.glVersion
    

    def isVertexBufferObjectSupport(self) -> bool:
        return False
    

    def isTextureSizeValid(self, widthAndHeight: int) -> bool:
        return True
from org.allbinary.logic.string.StringUtil import StringUtil


OpenGLCapabilities.instance = OpenGLCapabilities()

