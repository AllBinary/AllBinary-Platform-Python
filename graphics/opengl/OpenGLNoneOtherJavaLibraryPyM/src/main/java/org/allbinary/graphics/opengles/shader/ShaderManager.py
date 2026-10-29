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



class ShaderManager:
    instance: ShaderManager = None

    def _init_fields(self) -> None:
        self.LOAD_SHADER: str = "loadShader"
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.GL_VERTEX_SHADER: int = None
        self.GL_FRAGMENT_SHADER: int = None
    

    @staticmethod
    def getInstance() -> ShaderManager:
        return ShaderManager.instance
    

    def __init__(self, GL_VERTEX_SHADER: int, GL_FRAGMENT_SHADER: int) -> None:
        self._init_fields()
        self.GL_VERTEX_SHADER = GL_VERTEX_SHADER
        self.GL_FRAGMENT_SHADER = GL_FRAGMENT_SHADER
    

    def load(self, gl: GL10, resource: str, shaderAsStringArray: list[str], shaderType: int) -> int:
        return -1
    

    def loadShader(self, gl: GL10, resource: str, stringList: BasicArrayList, shaderType: int) -> int:
        return -1
# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


ShaderManager.instance = ShaderManager(-1, -1)

