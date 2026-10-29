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
# package org.allbinary.game.configuration.feature

from __future__ import annotations

# from javax.microedition.lcdui.ItemStateListener import ItemStateListener
from org.allbinary.util.BasicArrayListD import BasicArrayListD


class GameFeatureItemStateListener(ItemStateListener):
    toggleList: BasicArrayList = BasicArrayListD()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameOptionsForm: GameOptionsForm = None
    

    def __init__(self, gameOptionsForm: GameOptionsForm) -> None:
        from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
        self._init_fields()
        self.gameOptionsForm = gameOptionsForm
        gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        GameFeatureItemStateListener.add(gameFeatureFactory.ARTIFICIAL_INTELLEGENCE_PROCESSOR)
        GameFeatureItemStateListener.add(gameFeatureFactory.COLLIDABLE_INTERFACE_LAYER_PROCESSOR)
        GameFeatureItemStateListener.add(gameFeatureFactory.DAMAGE_FLOATERS)
        GameFeatureItemStateListener.add(gameFeatureFactory.DROPPED_ITEMS)
        GameFeatureItemStateListener.add(gameFeatureFactory.GAME_INPUT_LAYER_PROCESSOR)
        GameFeatureItemStateListener.add(gameFeatureFactory.HEALTH_BARS)
        GameFeatureItemStateListener.add(gameFeatureFactory.SOUND)
        GameFeatureItemStateListener.add(gameFeatureFactory.TICKABLE_LAYER_PROCESSOR)
    

    @staticmethod
    def add(gameFeature: GameFeature) -> None:
        if not GameFeatureItemStateListener.toggleList.contains(gameFeature):
            GameFeatureItemStateListener.toggleList.add(gameFeature)
    

    def itemStateChanged(self, item: Item) -> None:
        from org.allbinary.game.configuration.feature.GameFeatureUtil import GameFeatureUtil
        try:
            itemLabel: str = item.getLabel()
            self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().ITEM_LABEL).append(itemLabel)), self, "itemStateChanged")
            if isinstance(item, GameConfigurationGauge):
                GameConfigurationUtil.getInstance().change(self.gameOptionsForm, item)
            elif isinstance(item, ChoiceGroup):
                gameFeatureUtil: GameFeatureUtil = GameFeatureUtil.getInstance()
                if gameFeatureUtil.isExclusive(itemLabel):
                    gameFeatureUtil.updateExclusiveForChoiceGroup(item)
                else:
                    gameFeatureUtil.updateMultiple(item)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "itemStateChanged", e)
# from javax.microedition.lcdui.ChoiceGroup import ChoiceGroup
# from javax.microedition.lcdui.Item import Item
from org.allbinary.game.configuration.GameConfigurationGauge import GameConfigurationGauge
from org.allbinary.game.configuration.GameConfigurationUtil import GameConfigurationUtil
from org.allbinary.game.configuration.GameOptionsForm import GameOptionsForm
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


