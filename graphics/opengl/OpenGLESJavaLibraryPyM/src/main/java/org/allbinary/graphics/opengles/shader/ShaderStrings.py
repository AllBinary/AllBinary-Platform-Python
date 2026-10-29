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



class ShaderStrings:
    instance: ShaderStrings = None

    def _init_fields(self) -> None:
        self.NO_PROGRAM_HANDLE: str = "No program handle"
        self.UNIFORM_BLOCK_HANDLE: str = "Uniform Block Handle: "
        self.UNIFORM_HANDLE: str = "Uniform Handle: "
        self.UNIFORM_ATTRIBUTE_HANDLE: str = "Uniform Attribute Handle: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ShaderStrings:
        return ShaderStrings.instance


ShaderStrings.instance = ShaderStrings()

