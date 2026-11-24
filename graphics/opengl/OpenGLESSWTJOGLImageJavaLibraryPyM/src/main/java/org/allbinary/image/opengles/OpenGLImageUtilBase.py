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
# package org.allbinary.image.opengles

from __future__ import annotations



class OpenGLImageUtilBase:
    

    def paint_j3(self, alphaBitmap: OpenGLBitmap, originalBitmap: OpenGLBitmap, index: int) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        raise RuntimeError()
    

    def paint_j4(self, colorBitmap: OpenGLBitmap, originalBitmap: OpenGLBitmap, alpha: int, basicColor: BasicColor) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from org.allbinary.graphics.color.BasicColor import BasicColor
        raise RuntimeError()

    def paint(self, *args):
        return getattr(self, "paint_j" + str(len(args)))(*args)
    

    # throws IOException
    def createImage(self, name: str) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        raise RuntimeError()
    

    # throws Exception
    def createImageFromInputStream(self, inputStream: InputStream) -> OpenGLBitmap:
        from java.io.InputStream import InputStream
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        raise RuntimeError()
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
# from org.allbinary.graphics.color.BasicColor import BasicColor


