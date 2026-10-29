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
# package org.allbinary.game.configuration.event

from __future__ import annotations

from org.allbinary.game.configuration.event.GameFeatureListenerInterface import GameFeatureListenerInterface


class BaseChangedGameFeatureListener(GameFeatureListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameFeatureUtil: GameFeatureUtil = GameFeatureUtil.getInstance()
        self.list_: BasicArrayList = BasicArrayListD()
        self.changed: bool = True

    def __init__(self) -> None:
        self._init_fields()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(CommonStrings.getInstance().NOT_IMPLEMENTED, self)
    

    def onGameFeatureChange(self, gameFeatureEvent: GameFeatureEvent) -> None:
        self.logUtil.putF(str(StringMaker().append(self.gameFeatureUtil.GAME_FEATURE_CHANGED).append(gameFeatureEvent.getWhatChanged())), self, self.gameFeatureUtil.ON_GAME_FEATURE_CHANGE)
        self.list_.add(gameFeatureEvent.getGameOption())
        self.setChanged(True)
    

    def add(self, gameFeature: Feature) -> None:
        self.list_.add(gameFeature)
    

    def remove(self, gameFeature: Feature) -> None:
        self.list_.remove(gameFeature)
    

    def setChanged(self, initialized: bool) -> None:
        self.changed = initialized
        if not self.isChanged():
            self.list_.clear()
    

    def isChangedFeature(self, gameFeature: Feature) -> bool:
        isChanged: bool = self.list_.contains(gameFeature)
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("GameFeature: ")
        stringBuffer.append(StringUtil.getInstance().toString(gameFeature))
        stringBuffer.append(" isFeature: ")
        stringBuffer.appendboolean(Features.getInstance().isFeature(gameFeature))
        stringBuffer.append(" isChanged: ")
        stringBuffer.appendboolean(isChanged)
        self.logUtil.putF(str(stringBuffer), self, "isChanged")
        return isChanged
    

    def isChanged(self) -> bool:
        return self.changed
from org.allbinary.game.configuration.feature.Feature import Feature
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureUtil import GameFeatureUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


