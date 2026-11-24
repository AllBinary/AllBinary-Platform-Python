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



class GameFeatureImageCacheFactory:
    

    @staticmethod
    def getInstance() -> ImageCache:
        from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
        return ImageCacheFactory.getInstance()
    

    @staticmethod
    def init() -> None:
        from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
        ImageCacheFactory.init()
    

    @staticmethod
    def releaseAll() -> None:
        from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
        ImageCacheFactory.getInstance().releaseAll()


