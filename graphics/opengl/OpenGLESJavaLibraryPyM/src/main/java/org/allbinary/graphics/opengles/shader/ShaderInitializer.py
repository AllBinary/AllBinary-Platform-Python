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



class ShaderInitializer:
    instance: ShaderInitializer = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ShaderInitializer:
        return ShaderInitializer.instance
    

    def init(self, gl: GL10, shader: list[Shader], attributeArray: list[str]) -> int:
        return -1
# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.string.CommonStrings import CommonStrings


ShaderInitializer.instance = ShaderInitializer()

