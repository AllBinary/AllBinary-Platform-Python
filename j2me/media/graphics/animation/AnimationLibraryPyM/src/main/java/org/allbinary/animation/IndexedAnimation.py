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

from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.IndexedAnimationInterface import IndexedAnimationInterface


class IndexedAnimation(Animation, IndexedAnimationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.animationBehaviorP: AnimationBehavior = None
    

    def __init__(self, animationBehavior: AnimationBehavior) -> None:
        super().__init__()
        self._init_fields()
        self.animationBehaviorP = animationBehavior
    

    def getAnimationBehavior(self) -> AnimationBehavior:
        return self.animationBehaviorP
    

    def reset(self) -> None:
        self.animationBehaviorP.reset()
        self.setFrame(0)
    

    def setFrame(self, index: int) -> None:
        pass
    

    def getFrame(self) -> int:
        return 0
    

    # throws Exception
    def getAnimationSize(self) -> int:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def getSize(self) -> int:
        return 0
    

    def previousFrame(self) -> None:
        pass
    

    def isLastFrame(self) -> bool:
        if self.getFrame() == self.getSize() - 1:
            return True
        else:
            return False
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def setState(self, indexedAnimation: IndexedAnimation) -> None:
        self.setFrame(indexedAnimation.getFrame())
        self.setDx(indexedAnimation.getDx())
        self.setDy(indexedAnimation.getDy())
    

    def getWidth(self) -> int:
        return 0
    

    def getHeight(self) -> int:
        return 0
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.string.CommonStrings import CommonStrings


