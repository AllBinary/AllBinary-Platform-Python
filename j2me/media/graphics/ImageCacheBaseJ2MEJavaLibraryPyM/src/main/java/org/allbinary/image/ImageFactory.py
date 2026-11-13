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

from java.lang.JavaRuntimeStatic import lazy_static


#ImageCacheBaseJavaLibrary - J2ME
class ImageFactory:
    instance: ImageFactory = None
    

    @staticmethod
    def getInstance() -> ImageFactory:
        return ImageFactory.instance
    

    # throws Exception
    def createImageUrl(self, url: str) -> Image:
        from javax.microedition.lcdui.Image import Image
        return Image.createImage(url)
    

    # throws Exception
    def createImage(self, caller: str, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.MIDPUtil import MIDPUtil
        return MIDPUtil.getInstance().createImageWH(width, height)
    

    # throws Exception
    def createImageFromInputStream(self, key: object, inputStream: InputStream) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.MIDPUtil import MIDPUtil
        image: Image = MIDPUtil.getInstance().createImageFromInputStream(inputStream)
        return image
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def createImageFromInputStream(self, inputStream: InputStream) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.MIDPUtil import MIDPUtil
        return MIDPUtil.getInstance().createImageFromInputStream(inputStream)
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.MIDPUtil import MIDPUtil


def _ImageFactory_instance() -> object:
    return ImageFactory()

lazy_static(ImageFactory, "instance", _ImageFactory_instance)

