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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput


@java_inherited_overloads
class GameInputProcessorComposite(PlayerGameInput):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("name", None)
        vars(self).setdefault("gameInputProcessorInterface", None)
        vars(self).setdefault("NAME_LABEL", None)

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "gameInputProcessorInterface" not in vars(self): self.gameInputProcessorInterface: GameInputProcessorInterface = None
        self.NAME_LABEL: str = " GameInputProcessorInterface: "
    

    def __init__(self, name: str, gameInputProcessorInterface: GameInputProcessorInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        super().__init__(BasicArrayListD(), BasicArrayListD(), -1)
        __class__._init_fields(self)
        self.name = name
        self.gameInputProcessorInterface = gameInputProcessorInterface
    

    def update(self) -> None:
        with self._lock:
            return __class__.__dict__["_update_unlocked"].__get__(self, __class__)()

    def _update_unlocked(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            list_: BasicArrayList = self.getGameKeyEventList()
            self.gameInputProcessorInterface.onInput(list_)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        return str(StringMaker().append(java_super_call(super(), "toString")).append(self.NAME_LABEL).append(self.name))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


