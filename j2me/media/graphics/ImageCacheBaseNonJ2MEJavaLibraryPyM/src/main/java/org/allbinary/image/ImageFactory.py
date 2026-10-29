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
# package org.allbinary.image

from __future__ import annotations



#ImageCacheBaseAndroidJavaLibrary
class ImageFactory:
    instance: ImageFactory = None
    

    @staticmethod
    def getInstance() -> ImageFactory:
        return ImageFactory.instance
    

    # throws Exception
    def createImageUrl(self, url: str) -> Image:
        return Image.createImage(url)
    

    # throws Exception
    def createImage(self, caller: str, width: int, height: int) -> Image:
        return Image.createImageWH(width, height)
    

    # throws Exception
    def createImageFromInputStream(self, key: object, inputStream: InputStream) -> Image:
        image: Image = Image.createImageFromInputStream(inputStream)
        return image
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def createImageFromInputStream(self, inputStream: InputStream) -> Image:
        return Image.createImageFromInputStream(inputStream)
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image


ImageFactory.instance = ImageFactory()

