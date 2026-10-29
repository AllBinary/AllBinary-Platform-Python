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
# package org.allbinary.device

from __future__ import annotations



class OpenGLESGraphicsCompositeFactory:
    instance: OpenGLESGraphicsCompositeFactory = None

    def _init_fields(self) -> None:
        self.openGLESGraphicsFactory: OpenGLESGraphicsFactory = OpenGLESGraphicsFactory()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLESGraphicsCompositeFactory:
        return OpenGLESGraphicsCompositeFactory.instance
    

    def set(self, openGLESGraphicsFactory: OpenGLESGraphicsFactory) -> None:
        self.openGLESGraphicsFactory = openGLESGraphicsFactory
    

    def get(self) -> OpenGLESGraphicsFactory:
        return self.openGLESGraphicsFactory
from org.allbinary.device.OpenGLESGraphicsFactory import OpenGLESGraphicsFactory


OpenGLESGraphicsCompositeFactory.instance = OpenGLESGraphicsCompositeFactory()

