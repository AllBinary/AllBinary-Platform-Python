# Generated Code Do Not Modify
# package org.allbinary.game.terrain

from __future__ import annotations

from org.allbinary.game.terrain.TerrainEventListenerInterface import TerrainEventListenerInterface


class TerrainEventListener(TerrainEventListenerInterface):

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onTerrainEvent(self, terrainEvent: TerrainEvent) -> None:
        self.list_.clear()
        self.list_.add(terrainEvent)
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


