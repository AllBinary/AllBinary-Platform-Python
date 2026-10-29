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
# package org.allbinary.graphics.opengles.renderer

from __future__ import annotations



class AllBinaryRendererBase3:

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def update(self, gl: GL10) -> None:
        while self.list_.size() > 0:
            openGLESImage: OpenGLESImage = self.list_.removeAt(0)
            if openGLESImage is not None:
                openGLESImage.set(gl)
    

    def add(self, image: Image) -> None:
        self.list_.add(image)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


