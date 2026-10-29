# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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



class GameAdStateBase:

    def _init_fields(self) -> None:
        self.adConfigurationP: AdConfiguration = None
        self.advertisementsP: Advertisements = Advertisements()
        self.okayToShowAdsP: bool = False
    

    def __init__(self, adConfiguration: AdConfiguration) -> None:
        self._init_fields()
        self.adConfigurationP = adConfiguration
    

    def initViewArray(self, viewArray: list[object]) -> None:
        pass
    

    def onStart(self, anyType: object) -> None:
        self.init()
    

    def init(self) -> None:
        pass
    

    def isShowingAtLocation(self, location: int) -> bool:
        return False
    

    def isShowingAt(self) -> bool:
        return False
    

    def show(self) -> None:
        pass
    

    def hide(self) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def processAdState(self, gameState: GameState, gameType: GameType) -> None:
        pass
    

    def processPageAdState(self) -> None:
        pass
    

    # throws Exception
    def playingAdState(self) -> None:
        pass
    

    # throws Exception
    def playingAdStateWH(self, width: int, height: int) -> None:
        pass
    

    # throws Exception
    def notPlayingAdState(self) -> None:
        pass
    

    def setGameIsReady(self, gameIsReady: bool) -> None:
        pass
    

    def isGameIsReady(self) -> bool:
        return False
    

    def getAdvertisements(self) -> Advertisements:
        return self.advertisementsP
    

    def getAdConfiguration(self) -> AdConfiguration:
        return self.adConfigurationP
    

    def isOkayToShowPageAd(self) -> bool:
        return False
    

    def setOkayToShowAds(self, okayToShowAds: bool) -> None:
        self.okayToShowAdsP = okayToShowAds
    

    def isOkayToShowAds(self) -> bool:
        return self.okayToShowAdsP
    

    def isEnabled(self) -> bool:
        return False
from org.allbinary.game.GameType import GameType
from org.allbinary.game.state.GameState import GameState
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.business.advertisement.Advertisements import Advertisements


