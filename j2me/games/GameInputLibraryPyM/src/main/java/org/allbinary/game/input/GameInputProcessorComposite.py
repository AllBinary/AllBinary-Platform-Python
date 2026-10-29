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
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput


class GameInputProcessorComposite(PlayerGameInput):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.name: str = None
        self.gameInputProcessorInterface: GameInputProcessorInterface = None
        self.NAME_LABEL: str = " GameInputProcessorInterface: "
    

    def __init__(self, name: str, gameInputProcessorInterface: GameInputProcessorInterface) -> None:
        super().__init__(BasicArrayListD(), BasicArrayListD(), -1)
        self._init_fields()
        self.name = name
        self.gameInputProcessorInterface = gameInputProcessorInterface
    

    def update(self) -> None:
        with self._lock:
            return self._update_unlocked()

    def _update_unlocked(self) -> None:
        try:
            list_: BasicArrayList = self.getGameKeyEventList()
            self.gameInputProcessorInterface.onInput(list_)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
    

    def toString(self) -> str:
        return str(StringMaker().append(str(super())).append(self.NAME_LABEL).append(self.name))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


