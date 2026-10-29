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
# package org.allbinary.game.displayable

from __future__ import annotations



class GameLevelDisplayChangeEventListenersFactory:
    instance: GameLevelDisplayChangeEventListenersFactory = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameLevelDisplayChangeEventListenersFactory:
        return GameLevelDisplayChangeEventListenersFactory.instance
    

    def add(self, displayChangeEventListener: DisplayChangeEventListener) -> None:
        self.list_.add(displayChangeEventListener)
        DisplayChangeEventHandler.getInstance().addListenerInterface(displayChangeEventListener)
    

    def clear(self) -> None:
        displayChangeEventHandler: BasicEventHandler = DisplayChangeEventHandler.getInstance()
        displayChangeEventListener: DisplayChangeEventListener = None
        index = self.list_.size()
        while (index := index - 1) >= 0:
            displayChangeEventListener = self.list_.objectArray[index]
            displayChangeEventHandler.removeListener(displayChangeEventListener)
        self.list_.clear()
from org.allbinary.graphics.displayable.event.DisplayChangeEventHandler import DisplayChangeEventHandler
from org.allbinary.graphics.displayable.event.DisplayChangeEventListener import DisplayChangeEventListener
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


GameLevelDisplayChangeEventListenersFactory.instance = GameLevelDisplayChangeEventListenersFactory()

