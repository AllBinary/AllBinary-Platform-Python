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


class BaseAnimationInterfaceFactoryInterfaceComposite(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.basicAnimationInterfaceFactoryInterfaceArray: list[BasicAnimationInterfaceFactoryInterface] = None
    

    def __init__(self, basicAnimationInterfaceFactoryInterfaceArray: list[BasicAnimationInterfaceFactoryInterface]) -> None:
        self._init_fields()
        self.basicAnimationInterfaceFactoryInterfaceArray = basicAnimationInterfaceFactoryInterfaceArray
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
        return NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def getBasicAnimationInterfaceFactoryInterfaceArray(self) -> list[BasicAnimationInterfaceFactoryInterface]:
        return self.basicAnimationInterfaceFactoryInterfaceArray
    

    def setBasicAnimationInterfaceFactoryInterfaceArray(self, basicAnimationInterfaceFactoryInterfaceArray: list[BasicAnimationInterfaceFactoryInterface]) -> None:
        self.basicAnimationInterfaceFactoryInterfaceArray = basicAnimationInterfaceFactoryInterfaceArray
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.media.ScaleProperties import ScaleProperties


