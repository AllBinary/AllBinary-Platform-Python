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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

import threading
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
from org.allbinary.game.layer.special.SpecialGameInputFactory import SpecialGameInputFactory


class CheatGameInputProcessor(PlayerGameInput):
    inputProcessor: SpecialGameInputInterface = SpecialGameInputFactory.NO_SPECIAL_GAME_INPUT
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.PROCESS_GAME: str = "processGame"
        self.gameCanvas: AllBinaryGameCanvas = None
        self.gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        super().__init__(BasicArrayListD(), BasicArrayListD(), -1)
        self._init_fields()
        self.gameCanvas = gameCanvas
    

    def update(self) -> None:
        with self._lock:
            return self._update_unlocked()

    def _update_unlocked(self) -> None:
        try:
            gameLayerManager: AllBinaryGameLayerManager = self.gameCanvas.getLayerManager()
            list_: BasicArrayList = self.getGameKeyEventList()
            size: int = list_.size()
            for index in range(0, size):
                anyType: object = list_.objectArray[index]
                key: int = GameKeyEventUtil.getKey(anyType)
                if key == self.gameKeyFactory.LEVEL_DOWN.getId():
                    CheatGameInputProcessor.inputProcessor.strafeLeft()
                    break
                elif key == self.gameKeyFactory.LEVEL_UP.getId():
                    CheatGameInputProcessor.inputProcessor.strafeRight()
                    break
                if key == self.gameKeyFactory.LEFT.getId():
                    CheatGameInputProcessor.inputProcessor.left()
                    break
                elif key == self.gameKeyFactory.RIGHT.getId():
                    CheatGameInputProcessor.inputProcessor.right()
                    break
                elif key == self.gameKeyFactory.UP.getId():
                    CheatGameInputProcessor.inputProcessor.up()
                    break
                elif key == self.gameKeyFactory.DOWN.getId():
                    CheatGameInputProcessor.inputProcessor.down()
                    break
                elif key == self.gameKeyFactory.KEY_NUM1.getId():
                    CheatGameInputProcessor.inputProcessor.special1(gameLayerManager, GameKeyEvent.NONE)
                    break
                elif key == self.gameKeyFactory.KEY_NUM3.getId():
                    CheatGameInputProcessor.inputProcessor.special2(gameLayerManager, GameKeyEvent.NONE)
                    break
            list_.clear()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventUtil import GameKeyEventUtil
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.special.SpecialGameInputInterface import SpecialGameInputInterface
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


