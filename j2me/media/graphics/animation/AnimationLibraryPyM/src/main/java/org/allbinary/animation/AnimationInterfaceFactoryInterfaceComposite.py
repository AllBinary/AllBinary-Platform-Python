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
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class AnimationInterfaceFactoryInterfaceComposite(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface] = None
    

    def __init__(self, basicAnimationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface]) -> None:
        self._init_fields()
        self.animationInterfaceFactoryInterfaceArray = basicAnimationInterfaceFactoryInterfaceArray
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
        return NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def getAnimationInterfaceFactoryInterfaceArray(self) -> list[AnimationInterfaceFactoryInterface]:
        return self.animationInterfaceFactoryInterfaceArray
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.media.ScaleProperties import ScaleProperties


