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



class Shader:

    def _init_fields(self) -> None:
        self.shaderName: str = None
        self.shaderStringList: BasicArrayList = None
        self.shaderAsString: str = None
        self.shaderHandle: int = 0

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.util.BasicArrayList import BasicArrayList


