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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from org.allbinary.game.ag.ai.KeyPressesAI import KeyPressesAI


class MultiKeyPressesAI(KeyPressesAI):

    def _init_fields(self) -> None:
        self.toggleTimeHelper: TimeDelayHelper = TimeDelayHelper(600)
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(hashtable, ownerLayerInterface, gameInput)
        self._init_fields()
        self.update()
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        pass
    

    # throws Exception
    def update(self) -> None:
        gameInput: GameInput = self.getGameInput()
        keys: list[int] = self.keys
        size: int = len(keys)
        if self.isOn():
            for index in range(0, size):
                key: int = int(keys[index])
                if key != -1:
                    gameInput.add(self.gameKeyEventFactory.getInstanceForKey(self, key))
        else:
            for index in range(0, size):
                key: int = int(keys[index])
                if key != -1:
                    gameInput.addForRemoval(self.gameKeyEventFactory.getInstanceForKey(self, key))
    

    # throws Exception
    def toggle(self) -> None:
        if self.toggleTimeHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            super().toggle()
            self.update()
    

    # throws Exception
    def disable(self) -> None:
        if self.toggleTimeHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            super().disable()
            self.update()
    

    # throws Exception
    def enable(self) -> None:
        if self.toggleTimeHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            super().enable()
            self.update()
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable


