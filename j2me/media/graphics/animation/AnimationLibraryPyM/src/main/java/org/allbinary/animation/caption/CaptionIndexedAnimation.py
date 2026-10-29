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
# package org.allbinary.animation.caption

from __future__ import annotations

from org.allbinary.animation.IndexedAnimation import IndexedAnimation


class CaptionIndexedAnimation(IndexedAnimation):

    def _init_fields(self) -> None:
        self.animationInterface: Animation = None
        self.movieIndexedAnimationInterface: IndexedAnimation = None
        self.captionDx: int = None
        self.captionDy: int = None
        self.dx: int = None
        self.dy: int = None
        self.time: int = None
        self.END_EVENT: AllBinaryEventObject = None
        self.timeDelayHelper: TimeDelayHelper = None
        self.player: Player = None
    

    def __init__(self, animationInterface: Animation, movieIndexedAnimationInterface: IndexedAnimation, player: Player, captionDx: int, captionDy: int, dx: int, dy: int, time: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.animationInterface = animationInterface
        self.movieIndexedAnimationInterface = movieIndexedAnimationInterface
        self.captionDx = captionDx
        self.captionDy = captionDy
        self.dx = dx
        self.dy = dy
        self.time = time
        self.END_EVENT = AllBinaryEventObject(self)
        timePerFrame: int = int(self.time / self.getSize())
        self.timeDelayHelper = TimeDelayHelper(timePerFrame)
        self.player = player
        self.player.start()
    

    # throws Exception
    def nextFrame(self) -> None:
        if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            self.movieIndexedAnimationInterface.nextFrame()
        if self.isLastFrame():
            AnimationEventHandler.getInstance().fireEvent(self.END_EVENT)
    

    def isLastFrame(self) -> bool:
        if self.movieIndexedAnimationInterface.getFrame() == self.getSize() - 1:
            return True
        else:
            return False
    

    def previousFrame(self) -> None:
        self.movieIndexedAnimationInterface.previousFrame()
    

    def setFrame(self, index: int) -> None:
        self.movieIndexedAnimationInterface.setFrame(index)
    

    def getFrame(self) -> int:
        return self.movieIndexedAnimationInterface.getFrame()
    

    def getSize(self) -> int:
        return self.movieIndexedAnimationInterface.getSize()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.animationInterface.paintXY(graphics, x + self.captionDx, y + self.captionDy)
        self.movieIndexedAnimationInterface.paintXY(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        self.animationInterface.paintThreedXYZ(graphics, x + self.captionDx, y + self.captionDy, z)
        self.movieIndexedAnimationInterface.paintThreedXYZ(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy, z)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.media.Player import Player
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.animation.AnimationEventHandler import AnimationEventHandler
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


