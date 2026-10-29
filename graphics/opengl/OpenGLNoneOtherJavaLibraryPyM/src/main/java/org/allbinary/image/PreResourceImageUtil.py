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
# package org.allbinary.image

from __future__ import annotations



class PreResourceImageUtil:
    instance: PreResourceImageUtil = None
    

    @staticmethod
    def getInstance() -> PreResourceImageUtil:
        return PreResourceImageUtil.instance
    

    def encapsulate(self, image: Image) -> Image:
        return image
    

    def updateGL(self, gl: GL, image: Image) -> None:
        pass
    

    def update(self, graphics: Graphics, image: Image) -> None:
        pass
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image


PreResourceImageUtil.instance = PreResourceImageUtil()

