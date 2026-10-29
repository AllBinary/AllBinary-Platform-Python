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

from org.allbinary.image.ImageCache import ImageCache


#OpenGLESNullImageJavaLibrary
class OpenGLImageCacheFactory:
    IMAGE_CACHE: ImageCache = ImageCache.NULL_IMAGE_CACHE
    

    @staticmethod
    def getInstance() -> ImageCache:
        return OpenGLImageCacheFactory.IMAGE_CACHE
    

    @staticmethod
    def init() -> None:
        if OpenGLImageCacheFactory.IMAGE_CACHE is None:
            pass


