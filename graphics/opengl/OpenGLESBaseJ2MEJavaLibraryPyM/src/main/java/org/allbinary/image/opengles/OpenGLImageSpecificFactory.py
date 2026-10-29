#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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



class OpenGLImageSpecificFactory:
    instance: OpenGLImageSpecificFactory = None

    def _init_fields(self) -> None:
        self.imageFactory: OpenGLImageFactory = OpenGLImageFactory.NULL_OPENGL_IMAGE_FACTORY
        self.updating: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLImageSpecificFactory:
        return OpenGLImageSpecificFactory.instance
    

    def setImageFactory(self, imageFactory: OpenGLImageFactory) -> None:
        self.imageFactory = imageFactory
        PreLogUtil.put(str(StringMaker().append("Selected Image Factory: ").append(StringUtil.getInstance().toString(self.imageFactory))), self, "setImageFactory")
    

    def getImageFactory(self) -> OpenGLImageFactory:
        return self.imageFactory
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.image.opengles.OpenGLImageFactory import OpenGLImageFactory


OpenGLImageSpecificFactory.instance = OpenGLImageSpecificFactory()

