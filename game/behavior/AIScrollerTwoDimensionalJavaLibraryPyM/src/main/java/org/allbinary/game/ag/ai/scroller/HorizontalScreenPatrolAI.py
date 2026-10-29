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

from org.allbinary.game.ai.BasicAI import BasicAI
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


class HorizontalScreenPatrolAI(BasicAI):
    SOUND: int = SmallIntegerSingletonFactory.getInstance().getAt(433)

    def _init_fields(self) -> None:
        self.keyDirection: int = Canvas.LEFT
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.firingX: int = self.displayInfoSingleton.getLastHalfWidth()
        self.firedIndex: int = 0
        self.MAX_FIRE: int = 28
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(240)
        self.secondaryPlayerQueue: PlayerQueue = SecondaryPlayerQueueFactory.getInstance()
        self.sound: Sound = None
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.sound = hashtable.get(HorizontalScreenPatrolAI.SOUND)
        if self.sound is None:
            raise Exception("No Sound Provided!!")
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        super().processKeyAI(self.keyDirection)
        if self.timeDelayHelper.isTimeTNT():
            layerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
            currentOwnerLayerX: int = layerInterface.getXP()
            if currentOwnerLayerX < -layerInterface.getWidth():
                y: int = MyRandomFactory.getInstance().getAbsoluteNextIntAllowZero(50)
                layerInterface.setPosition(self.displayInfoSingleton.getLastWidth() + layerInterface.getWidth() + 50, y, layerInterface.getZP())
                self.firedIndex = 0
                self.firingX = self.displayInfoSingleton.getLastHalfWidth() + MyRandomFactory.getInstance().getNextInt(self.displayInfoSingleton.getLastHalfWidth())
                self.secondaryPlayerQueue.add(self.sound)
            if currentOwnerLayerX < self.firingX and currentOwnerLayerX > -layerInterface.getWidth():
                super().processKeyAI(Canvas.KEY_NUM1)
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
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.audio.PlayerQueue import PlayerQueue
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable


