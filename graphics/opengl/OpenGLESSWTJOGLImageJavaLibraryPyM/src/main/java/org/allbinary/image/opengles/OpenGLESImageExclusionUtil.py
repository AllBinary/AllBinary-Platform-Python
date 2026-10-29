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
        self.EXCLUSION: str = "font"
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> OpenGLESImageExclusionUtil:
        return OpenGLESImageExclusionUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def isCustomScaling(self, image: Image) -> bool:
        imageName: str = image.getName()
        isNormalScaling: bool = self.list_.size() == 0 or imageName.startswith(self.EXCLUSION)
        if isNormalScaling:
            return False
        else:
            size: int = self.list_.size()
            name: str = None
            for index in range(0, size):
                name = self.list_.get(index)
                if imageName.startswith(name):
                    isNormalScaling = True
        if isNormalScaling:
            return False
        else:
            return True
# from javax.microedition.lcdui.Image import Image
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


OpenGLESImageExclusionUtil.instance = OpenGLESImageExclusionUtil()

