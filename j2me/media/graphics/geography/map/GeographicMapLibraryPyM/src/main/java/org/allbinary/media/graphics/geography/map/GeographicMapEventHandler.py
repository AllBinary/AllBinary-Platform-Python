# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations

from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class GeographicMapEventHandler(BasicEventHandler):
    instance: GeographicMapEventHandler = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> GeographicMapEventHandler:
        return GeographicMapEventHandler.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addListener(self, gameLayer: AllBinaryGameLayer) -> None:
        if not self.list_.contains(gameLayer):
            self.list_.add(gameLayer)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        super().removeAllListeners()
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        self.list_.remove(eventListenerInterface)
        super().removeListener(eventListenerInterface)
    

    def fireEvent(self) -> None:
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                gameLayer: AllBinaryGameLayer = self.list_.get(index)
                gameLayer.move()
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


GeographicMapEventHandler.instance = GeographicMapEventHandler()

