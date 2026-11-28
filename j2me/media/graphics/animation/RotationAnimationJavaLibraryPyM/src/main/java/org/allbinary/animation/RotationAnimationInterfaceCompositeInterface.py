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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.IndexedAnimationInterfaceCompositeInterface import IndexedAnimationInterfaceCompositeInterface


# Java interface
@java_inherited_overloads
class RotationAnimationInterfaceCompositeInterface(IndexedAnimationInterfaceCompositeInterface):
    

    def getRotationAnimationInterface(self) -> RotationAnimation:
        raise NotImplementedError()
    

    def setFrame(self, index: int) -> None:
        raise NotImplementedError()


