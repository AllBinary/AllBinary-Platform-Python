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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory


@java_inherited_overloads
class IndexedAnimationBehaviorFactory(AnimationBehaviorFactory):
    def _java_defaults(self):
        vars(self).setdefault("frameDelayTime", 0)
        vars(self).setdefault("loopTotal", 0)

    def _init_fields(self) -> None:
        if "frameDelayTime" not in vars(self): self.frameDelayTime: int = 0
        if "loopTotal" not in vars(self): self.loopTotal: int = 0
    

    def __init__(self, loopTotal: int, frameDelayTime: int) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.loopTotal = loopTotal
        self.frameDelayTime = frameDelayTime
    

    def getOrCreateInstance(self) -> AnimationBehavior:
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        return IndexedAnimationBehavior(self.loopTotal, self.frameDelayTime)


