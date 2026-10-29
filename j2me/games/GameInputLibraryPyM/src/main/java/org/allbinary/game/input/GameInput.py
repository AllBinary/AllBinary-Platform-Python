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
# package org.allbinary.game.input

from __future__ import annotations

import threading


class GameInput:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameKeyEventList: BasicArrayList = None
        self.removalGameKeyEventList: BasicArrayList = None
        self.isRemoveDuplicateKeyPresses: bool = None
    

    def __init__(self, gameKeyEventList: BasicArrayList, removalGameKeyEventList: BasicArrayList) -> None:
        self._init_fields()
        self.gameKeyEventList = gameKeyEventList
        self.removalGameKeyEventList = removalGameKeyEventList
        self.isRemoveDuplicateKeyPresses = Features.getInstance().isFeature(InputFeatureFactory.getInstance().REMOVE_DUPLICATE_KEY_PRESSES)
    

    def add(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._add_unlocked(gameKeyEvent)

    def _add_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        if self.isRemoveDuplicateKeyPresses and self.gameKeyEventList.contains(gameKeyEvent):
            return
        if gameKeyEvent is not None:
            self.gameKeyEventList.add(gameKeyEvent)
        else:
            self.logUtil.putF("Danger Passed Null GameKeyEvent", self, self.commonStrings.ADD)
    

    def addForRemoval(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._addForRemoval_unlocked(gameKeyEvent)

    def _addForRemoval_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        self.removalGameKeyEventList.add(gameKeyEvent)
    

    def isForRemoval(self, gameKeyEvent: GameKeyEvent) -> bool:
        with self._lock:
            return self._isForRemoval_unlocked(gameKeyEvent)

    def _isForRemoval_unlocked(self, gameKeyEvent: GameKeyEvent) -> bool:
        return self.removalGameKeyEventList.contains(gameKeyEvent)
    

    def clear(self) -> None:
        with self._lock:
            return self._clear_unlocked()

    def _clear_unlocked(self) -> None:
        self.gameKeyEventList.clear()
    

    def removeNonAIInputGameKeyEvents(self) -> None:
        with self._lock:
            return self._removeNonAIInputGameKeyEvents_unlocked()

    def _removeNonAIInputGameKeyEvents_unlocked(self) -> None:
        list_: BasicArrayList = self.gameKeyEventList
        gameKeyEvent: GameKeyEvent = None
        index = list_.size()
        while (index := index - 1) >= 0:
            gameKeyEvent = list_.objectArray[index]
            if gameKeyEvent.getSourceId() != 1:
                list_.removeAt(index)
    

    def update(self) -> None:
        with self._lock:
            return self._update_unlocked()

    def _update_unlocked(self) -> None:
        removeList: BasicArrayList = self.removalGameKeyEventList
        list_: BasicArrayList = self.gameKeyEventList
        size: int = removeList.size()
        for index in range(0, size):
            anyType: object = removeList.objectArray[index]
            index2 = list_.size()
            while (index2 := index2 - 1) >= 0:
                if list_.objectArray[index2] == anyType:
                    list_.removeAt(index2)
        removeList.clear()
    

    def getRemovalGameKeyEventList(self) -> BasicArrayList:
        return self.removalGameKeyEventList
    

    def getGameKeyEventList(self) -> BasicArrayList:
        return self.gameKeyEventList
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


