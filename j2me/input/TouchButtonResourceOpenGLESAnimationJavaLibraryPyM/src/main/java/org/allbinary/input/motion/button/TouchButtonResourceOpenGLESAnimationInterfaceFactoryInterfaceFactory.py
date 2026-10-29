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

from org.allbinary.input.motion.button.TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory import TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory


class TouchButtonResourceOpenGLESAnimationInterfaceFactoryInterfaceFactory(TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory):
    

    def __init__(self) -> None:
        super().__init__("OpenGL TouchButton Animations")
    

    # throws Exception
    def init(self, level: int) -> None:
        super().initImageCache(OpenGLImageCacheFactory.getInstance(), level)
    

    def isFeature(self) -> bool:
        if Features.getInstance().isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            return True
        else:
            return False
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.image.opengles.OpenGLImageCacheFactory import OpenGLImageCacheFactory


