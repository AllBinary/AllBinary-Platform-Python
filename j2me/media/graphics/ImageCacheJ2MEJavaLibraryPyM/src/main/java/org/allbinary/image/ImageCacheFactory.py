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

from java.lang.JavaRuntimeStatic import lazy_static


class ImageCacheFactory:
    IMAGE_CACHE: ImageCache = None
    

    @staticmethod
    def getInstance() -> ImageCache:
        return ImageCacheFactory.IMAGE_CACHE
    

    @staticmethod
    def init() -> None:
        pass


def _ImageCacheFactory_IMAGE_CACHE() -> object:
    from org.allbinary.image.ImageCache import ImageCache
    return ImageCache()

lazy_static(ImageCacheFactory, "IMAGE_CACHE", _ImageCacheFactory_IMAGE_CACHE)

