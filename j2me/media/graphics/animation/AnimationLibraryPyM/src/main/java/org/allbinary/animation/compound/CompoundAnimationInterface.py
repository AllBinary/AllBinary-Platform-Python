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
# package org.allbinary.animation.compound

from __future__ import annotations

from org.allbinary.animation.AnimationInterface import AnimationInterface


# Java interface
class CompoundAnimationInterface(AnimationInterface):
    

    def nextAnimation(self) -> None:
        raise NotImplementedError()
    

    def previousAnimation(self) -> None:
        raise NotImplementedError()
    

    def setAnimation(self, index: int) -> None:
        raise NotImplementedError()
    

    def getCurrentAnimation(self) -> IndexedAnimation:
        raise NotImplementedError()
from org.allbinary.animation.IndexedAnimation import IndexedAnimation


