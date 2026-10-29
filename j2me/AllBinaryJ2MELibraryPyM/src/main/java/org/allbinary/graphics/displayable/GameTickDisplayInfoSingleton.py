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
# package org.allbinary.graphics.displayable

from __future__ import annotations



class GameTickDisplayInfoSingleton:
    instance: GameTickDisplayInfoSingleton = None

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.lastWidth: int = self.displayInfoSingleton.getLastWidth()
        self.lastHeight: int = self.displayInfoSingleton.getLastHeight()
        self.lastHalfWidth: int = self.displayInfoSingleton.getLastHalfWidth()
        self.lastHalfHeight: int = self.displayInfoSingleton.getLastHalfHeight()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameTickDisplayInfoSingleton:
        return GameTickDisplayInfoSingleton.instance
    

    def update(self) -> None:
        self.lastWidth = self.displayInfoSingleton.getLastWidth()
        self.lastHeight = self.displayInfoSingleton.getLastHeight()
        self.lastHalfWidth = self.displayInfoSingleton.getLastHalfWidth()
        self.lastHalfHeight = self.displayInfoSingleton.getLastHalfHeight()
    

    def getLastWidth(self) -> int:
        return self.lastWidth
    

    def getLastHeight(self) -> int:
        return self.lastHeight
    

    def getLastHalfWidth(self) -> int:
        return self.lastHalfWidth
    

    def getLastHalfHeight(self) -> int:
        return self.lastHalfHeight
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


GameTickDisplayInfoSingleton.instance = GameTickDisplayInfoSingleton()

