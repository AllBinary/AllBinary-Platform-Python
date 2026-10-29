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

from org.allbinary.game.ai.BasicAI import BasicAI


class KeyPressesAI(BasicAI):

    def _init_fields(self) -> None:
        self.on: bool = True
        self.keys: list[int] = None
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.keys = [None] * (hashtable.size())
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        size: int = len(objectArray)
        for index in range(0, size):
            self.keys[index] = hashtable.get(objectArray[index])
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.on:
            for index in range(0, len(self.keys)):
                super().processKeyAI(int(self.keys[index]))
    

    # throws Exception
    def toggle(self) -> None:
        if self.isOn():
            self.setOn(False)
        else:
            self.setOn(True)
    

    # throws Exception
    def disable(self) -> None:
        self.setOn(False)
    

    # throws Exception
    def enable(self) -> None:
        self.setOn(True)
    

    def setOn(self, on: bool) -> None:
        self.on = on
    

    def isOn(self) -> bool:
        return self.on
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.util.HashtableUtil import HashtableUtil
from org.allbinary.util.ABHashtable import ABHashtable


