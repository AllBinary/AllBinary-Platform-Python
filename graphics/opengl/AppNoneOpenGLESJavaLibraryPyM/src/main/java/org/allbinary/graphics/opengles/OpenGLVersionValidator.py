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
# package org.allbinary.graphics.opengles

from __future__ import annotations



class OpenGLVersionValidator:
    instance: OpenGLVersionValidator = None

    def _init_fields(self) -> None:
        self.EGL_CONTEXT_CLIENT_VERSION_VALUE: int = -1

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLVersionValidator:
        return OpenGLVersionValidator.instance
    

    def isGL31OrHigher(self) -> bool:
        return False
    

    def isAvailable(self, glVersionRequired: str) -> bool:
        return False
    

    def setShaderComposite(self, shaderComposite: ShaderComposite, anyType: object) -> None:
        pass
from org.allbinary.graphics.opengles.shader.ShaderComposite import ShaderComposite


OpenGLVersionValidator.instance = OpenGLVersionValidator()

