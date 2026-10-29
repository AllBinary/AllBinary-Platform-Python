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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.animation.resource.BaseResourceAnimationInterfaceFactoryInterfaceFactory import BaseResourceAnimationInterfaceFactoryInterfaceFactory


class TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory(BaseResourceAnimationInterfaceFactoryInterfaceFactory):
    

    @staticmethod
    def createFactory() -> TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory:
        return TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory("TouchButton Animations")
    

    def __init__(self, name: str) -> None:
        super().__init__(name, StdUtil.getInstance().createHashtable(), StdUtil.getInstance().createHashtable(), StdUtil.getInstance().createHashtable())
    

    # throws Exception
    def init(self, level: int) -> None:
        self.initImageCache(ImageCacheFactory.getInstance(), level)
    

    # throws Exception
    def initImageCache(self, imageCache: ImageCache, level: int) -> None:
        if self.isInitialized():
            return
        super().init(level)
    

    def isLoadingLevel(self, level: int) -> bool:
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if level == resourceLoadingLevelFactory.LOAD_TOUCH.getLevel():
            return True
        else:
            return super().isLoadingLevel(level)
    

    def isFeature(self) -> bool:
        if not Features.getInstance().isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            return True
        else:
            return False
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
from org.allbinary.logic.StdUtil import StdUtil


