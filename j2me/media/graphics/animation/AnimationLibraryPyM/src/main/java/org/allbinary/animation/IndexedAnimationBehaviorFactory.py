# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory


class IndexedAnimationBehaviorFactory(AnimationBehaviorFactory):

    def _init_fields(self) -> None:
        self.frameDelayTime: int = None
        self.loopTotal: int = None
    

    def __init__(self, loopTotal: int, frameDelayTime: int) -> None:
        super().__init__()
        self._init_fields()
        self.loopTotal = loopTotal
        self.frameDelayTime = frameDelayTime
    

    def getOrCreateInstance(self) -> AnimationBehavior:
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        return IndexedAnimationBehavior(self.loopTotal, self.frameDelayTime)


