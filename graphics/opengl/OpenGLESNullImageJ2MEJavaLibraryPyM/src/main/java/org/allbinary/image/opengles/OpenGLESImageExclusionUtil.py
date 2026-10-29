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



class OpenGLESImageExclusionUtil:
    instance: OpenGLESImageExclusionUtil = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLESImageExclusionUtil:
        return OpenGLESImageExclusionUtil.instance
    

    def isCustomScaling(self, image: Image) -> bool:
        return False
# from javax.microedition.lcdui.Image import Image
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


OpenGLESImageExclusionUtil.instance = OpenGLESImageExclusionUtil()

