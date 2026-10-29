# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.image.opengles

from __future__ import annotations

from org.allbinary.image.opengles.OpenGLESImageProcessor import OpenGLESImageProcessor


class ModifierOpenGLESImageProcessor(OpenGLESImageProcessor):
    instanceC: ModifierOpenGLESImageProcessor = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ModifierOpenGLESImageProcessor:
        return ModifierOpenGLESImageProcessor.instanceC


ModifierOpenGLESImageProcessor.instanceC = ModifierOpenGLESImageProcessor()

