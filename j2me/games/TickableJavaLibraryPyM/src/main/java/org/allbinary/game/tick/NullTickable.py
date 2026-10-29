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
# package org.allbinary.game.tick

from __future__ import annotations

from org.allbinary.game.tick.TickableInterface import TickableInterface


class NullTickable(TickableInterface):
    SINGLETON: NullTickable = None

    def _init_fields(self) -> None:
        self.NAME: str = "NulLTickable"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> NullTickable:
        return NullTickable.SINGLETON
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        pass
    

    def getName(self) -> str:
        return self.NAME
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


NullTickable.SINGLETON = NullTickable()

