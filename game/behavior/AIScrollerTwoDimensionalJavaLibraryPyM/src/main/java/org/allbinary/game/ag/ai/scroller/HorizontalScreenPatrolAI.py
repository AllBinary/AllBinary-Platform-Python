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
# package org.allbinary.game.ag.ai.scroller

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.ai.BasicAI import BasicAI


@java_inherited_overloads
class HorizontalScreenPatrolAI(BasicAI):
    SOUND: int = None
    def _java_defaults(self):
        vars(self).setdefault("keyDirection", 0)
        vars(self).setdefault("displayInfoSingleton", None)
        vars(self).setdefault("firingX", 0)
        vars(self).setdefault("firedIndex", 0)
        vars(self).setdefault("MAX_FIRE", 0)
        vars(self).setdefault("timeDelayHelper", None)
        vars(self).setdefault("secondaryPlayerQueue", None)
        vars(self).setdefault("sound", None)

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.keyDirection: int = Canvas.LEFT
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.firingX: int = self.displayInfoSingleton.getLastHalfWidth()
        self.firedIndex: int = 0
        self.MAX_FIRE: int = 28
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(240)
        self.secondaryPlayerQueue: PlayerQueue = SecondaryPlayerQueueFactory.getInstance()
        if "sound" not in vars(self): self.sound: Sound = None
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.media.audio.Sound import Sound
        from org.allbinary.util.ABHashtable import ABHashtable
        super().__init__(ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        self.sound = hashtable.get(HorizontalScreenPatrolAI.SOUND)
        if self.sound is None:
            raise Exception("No Sound Provided!!")
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        java_super_call(super(), "processKeyAI", self.keyDirection)
        if java_predicate(self.timeDelayHelper, "isTimeTNT"):
            layerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
            currentOwnerLayerX: int = layerInterface.getXP()
            if currentOwnerLayerX < -layerInterface.getWidth():
                y: int = MyRandomFactory.getInstance().getAbsoluteNextIntAllowZero(50)
                layerInterface.setPosition(self.displayInfoSingleton.getLastWidth() + layerInterface.getWidth() + 50, y, layerInterface.getZP())
                self.firedIndex = 0
                self.firingX = self.displayInfoSingleton.getLastHalfWidth() + MyRandomFactory.getInstance().getNextInt(self.displayInfoSingleton.getLastHalfWidth())
                self.secondaryPlayerQueue.add(self.sound)
            if currentOwnerLayerX < self.firingX and currentOwnerLayerX > -layerInterface.getWidth():
                java_super_call(super(), "processKeyAI", Canvas.KEY_NUM1)
                gameLayerManager: AllBinaryGameLayerManager = allBinaryLayerManager
                FIRE: int = (gameLayerManager.getGameInfo().getCurrentLevel() + 12) >> 2
                if FIRE > self.MAX_FIRE:
                    FIRE = self.MAX_FIRE
                if self.firedIndex > FIRE:
                    self.firedIndex = 0
                    self.firingX = -2147483648
                self.firedIndex += 1
    

    def nextDirection(self) -> None:
        pass
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
# from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.media.audio.PlayerQueue import PlayerQueue
# from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
# from org.allbinary.media.audio.Sound import Sound
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.util.ABHashtable import ABHashtable


def _HorizontalScreenPatrolAI_SOUND() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(433)

lazy_static(HorizontalScreenPatrolAI, "SOUND", _HorizontalScreenPatrolAI_SOUND)

