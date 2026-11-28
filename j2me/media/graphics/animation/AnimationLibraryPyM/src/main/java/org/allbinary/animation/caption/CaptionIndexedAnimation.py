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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.IndexedAnimation import IndexedAnimation


@java_inherited_overloads
class CaptionIndexedAnimation(IndexedAnimation):
    def _java_defaults(self):
        vars(self).setdefault("animationInterface", None)
        vars(self).setdefault("movieIndexedAnimationInterface", None)
        vars(self).setdefault("captionDx", 0)
        vars(self).setdefault("captionDy", 0)
        vars(self).setdefault("dx", 0)
        vars(self).setdefault("dy", 0)
        vars(self).setdefault("time", 0)
        vars(self).setdefault("END_EVENT", None)
        vars(self).setdefault("timeDelayHelper", None)
        vars(self).setdefault("player", None)

    def _init_fields(self) -> None:
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
        if "movieIndexedAnimationInterface" not in vars(self): self.movieIndexedAnimationInterface: IndexedAnimation = None
        if "captionDx" not in vars(self): self.captionDx: int = 0
        if "captionDy" not in vars(self): self.captionDy: int = 0
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
        if "time" not in vars(self): self.time: int = 0
        if "END_EVENT" not in vars(self): self.END_EVENT: AllBinaryEventObject = None
        if "timeDelayHelper" not in vars(self): self.timeDelayHelper: TimeDelayHelper = None
        if "player" not in vars(self): self.player: Player = None
    

    def __init__(self, animationInterface: Animation, movieIndexedAnimationInterface: IndexedAnimation, player: Player, captionDx: int, captionDy: int, dx: int, dy: int, time: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.media.Player import Player
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        super().__init__(animationBehavior)
        __class__._init_fields(self)
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
        from org.allbinary.animation.AnimationEventHandler import AnimationEventHandler
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            self.movieIndexedAnimationInterface.nextFrame()
        if java_predicate(self, "isLastFrame"):
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
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintXY(graphics, x + self.captionDx, y + self.captionDy)
        self.movieIndexedAnimationInterface.paintXY(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintThreedXYZ(graphics, x + self.captionDx, y + self.captionDy, z)
        self.movieIndexedAnimationInterface.paintThreedXYZ(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy, z)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.media.Player import Player
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.animation.AnimationEventHandler import AnimationEventHandler
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


