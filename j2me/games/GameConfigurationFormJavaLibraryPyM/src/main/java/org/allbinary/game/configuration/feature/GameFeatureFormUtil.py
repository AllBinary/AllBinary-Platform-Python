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



class GameFeatureFormUtil:
    instance: GameFeatureFormUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.meUtil: MEUtil = MEUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameFeatureFormUtil:
        return GameFeatureFormUtil.instance
    

    def getChoiceGroup(self, hashtable: ABHashtable[object, object], name: str, option: int) -> ChoiceGroup:
        from org.allbinary.game.configuration.feature.Features import Features
        stringMaker: StringMaker = StringMaker()
        choiceGroup: ChoiceGroup = ChoiceGroup(name, option, StringUtil.getInstance().getArrayInstance(), NullImage.NULL_IMAGE_ARRAY)
        list_: BasicArrayList = hashtable.get(name)
        features: Features = Features.getInstance()
        ADD_CHOICE: str = ": Adding Choice: "
        GET_CHOICE_GROUP: str = "getChoiceGroup"
        size: int = list_.size()
        for index in range(0, size):
            gameFeature: Feature = list_.objectArray[index]
            stringMaker.delete(0, stringMaker.length())
            self.logUtil.putF(str(stringMaker.append(name).append(ADD_CHOICE).append(str(gameFeature))), self, GET_CHOICE_GROUP)
            choiceGroup.append(str(gameFeature), NullImage.NULL_IMAGE)
            if features.isFeature(gameFeature):
                choiceGroup.setSelectedIndex(index, True)
        return choiceGroup
    

    def addChoiceGroup(self, form: CommandForm, hashtable: ABHashtable[object, object], option: int) -> None:
        stringMaker: StringMaker = StringMaker()
        ADDING_CHOICE_GROUP: str = "Adding Choice Group: "
        ADD_CHOICE_GROUP: str = "addChoiceGroup"
        size: int = hashtable.size()
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        name: str = None
        for index in range(0, size):
            name = objectArray[index]
            stringMaker.delete(0, stringMaker.length())
            self.logUtil.putF(str(stringMaker.append(ADDING_CHOICE_GROUP).append(name)), self, ADD_CHOICE_GROUP)
            self.meUtil.appendItem(form, self.getChoiceGroup(hashtable, name, option))
    

    # throws Exception
    def setDefault(self, form: CommandForm) -> None:
        from org.allbinary.game.configuration.feature.GameFeatureUtil import GameFeatureUtil
        size: int = form.size()
        for index in range(0, size):
            item: Item = form.get(index)
            if isinstance(item, GameConfigurationGauge):
                GameConfigurationUtil.getInstance().setDefault(item)
            elif isinstance(item, ChoiceGroup):
                GameFeatureUtil.getInstance().setDefault(item)
# from javax.microedition.lcdui.ChoiceGroup import ChoiceGroup
# from javax.microedition.lcdui.Item import Item
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.game.configuration.GameConfigurationGauge import GameConfigurationGauge
from org.allbinary.game.configuration.GameConfigurationUtil import GameConfigurationUtil
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm
from org.allbinary.logic.MEUtil import MEUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.HashtableUtil import HashtableUtil


GameFeatureFormUtil.instance = GameFeatureFormUtil()

