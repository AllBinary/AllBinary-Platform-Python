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

from org.allbinary.graphics.opengles.shader.ShaderInitializer import ShaderInitializer


class SimpleShaderInitializer(ShaderInitializer):
    instanceC: SimpleShaderInitializer = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> SimpleShaderInitializer:
        return SimpleShaderInitializer.instanceC


SimpleShaderInitializer.instanceC = SimpleShaderInitializer()

