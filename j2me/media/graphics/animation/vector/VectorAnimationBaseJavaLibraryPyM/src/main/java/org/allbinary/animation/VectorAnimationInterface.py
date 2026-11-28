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
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface
from org.allbinary.animation.IndexedAnimationInterface import IndexedAnimationInterface


# Java interface
@java_inherited_overloads
class VectorAnimationInterface(*java_bases(IndexedAnimationInterface, ColorCompositeInterface)):
    

    def getPoints(self, frame: int) -> list[list[int]]:
        raise NotImplementedError()


