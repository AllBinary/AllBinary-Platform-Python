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
# package org.allbinary.business.advertisement

from __future__ import annotations



class AdConfiguration:

    def _init_fields(self) -> None:
        self.INNERACTIVE: str = None
        self.LEADBOLT: str = None
        self.ADMOB: str = None
    

    def __init__(self, advertIdArray: list[object]) -> None:
        self._init_fields()
        self.INNERACTIVE = advertIdArray[0]
        self.ADMOB = advertIdArray[1]
        self.LEADBOLT = advertIdArray[2]
    

    def getValidAdSpots(self) -> list[Direction]:
        return [None] * (0)
    

    def process(self, gameState: GameState) -> None:
        pass
    

    def processDemo(self, state: int) -> None:
        pass
    

    def setShowAds(self) -> None:
        pass
    

    def setToggleAds(self, showAds: bool) -> None:
        pass
    

    def isShowAds(self) -> bool:
        return True
from org.allbinary.direction.Direction import Direction
from org.allbinary.game.state.GameState import GameState


