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



class GameFeatureUtil:
    instance: GameFeatureUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        self.ON_GAME_FEATURE_CHANGE: str = "onGameFeatureChange"
        self.GAME_FEATURE_CHANGED: str = "Game Feature Changed: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameFeatureUtil:
        return GameFeatureUtil.instance
    

    # throws Exception
    def setDefault(self, choiceGroup: ChoiceGroup) -> None:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.configuration.feature.Feature import Feature
        stringBuffer: StringMaker = StringMaker()
        METHOD_NAME: str = "setDefault"
        SELECTED_ARRAY_RETURN: str = "selectedArray_return["
        SELECTED_SEP: str = "] = "
        selectedArray_return: list[bool] = [False] * (choiceGroup.size())
        total: int = choiceGroup.getSelectedFlags(selectedArray_return)
        stringBuffer.append("Multiple Total Choices: ")
        stringBuffer.appendint(total)
        self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
        features: Features = Features.getInstance()
        for index in range(0, len(selectedArray_return)):
            isSelected: bool = selectedArray_return[index]
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(SELECTED_ARRAY_RETURN)
            stringBuffer.appendint(index)
            stringBuffer.append(SELECTED_SEP)
            stringBuffer.appendboolean(isSelected)
            self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
            selectedChoiceLabel: str = choiceGroup.getString(index)
            gameFeature: Feature = Feature.getInstance(selectedChoiceLabel)
            if features.isDefault(gameFeature):
                features.add(gameFeature)
                choiceGroup.setSelectedIndex(index, True)
            else:
                features.remove(gameFeature)
                choiceGroup.setSelectedIndex(index, False)
    

    # throws Exception
    def updateMultiple(self, choiceGroup: ChoiceGroup) -> None:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.configuration.feature.Feature import Feature
        stringBuffer: StringMaker = StringMaker()
        METHOD_NAME: str = "updateMultiple"
        SELECTED_ARRAY_RETURN: str = "selectedArray_return["
        SELECTED_SEP: str = "] = "
        selectedArray_return: list[bool] = [False] * (choiceGroup.size())
        total: int = choiceGroup.getSelectedFlags(selectedArray_return)
        stringBuffer.append("Multiple Total Choices: ")
        stringBuffer.appendint(total)
        self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
        features: Features = Features.getInstance()
        for index in range(0, len(selectedArray_return)):
            isSelected: bool = selectedArray_return[index]
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(SELECTED_ARRAY_RETURN)
            stringBuffer.appendint(index)
            stringBuffer.append(SELECTED_SEP)
            stringBuffer.appendboolean(isSelected)
            self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
            selectedChoiceLabel: str = choiceGroup.getString(index)
            gameFeature: Feature = Feature.getInstance(selectedChoiceLabel)
            if not isSelected and features.isFeature(gameFeature):
                features.remove(gameFeature)
            elif isSelected and not features.isFeature(gameFeature):
                features.add(gameFeature)
    

    # throws Exception
    def updateExclusiveForChoiceGroup(self, choiceGroup: ChoiceGroup) -> None:
        stringBuffer: StringMaker = StringMaker()
        METHOD_NAME: str = "updateExclusive"
        SELECTED_ARRAY_RETURN: str = "selectedArray_return["
        SELECTED_SEP: str = "] = "
        selectedArray_return: list[bool] = [False] * (choiceGroup.size())
        total: int = choiceGroup.getSelectedFlags(selectedArray_return)
        stringBuffer.append("Exclusive Total Choices: 1==")
        stringBuffer.appendint(total)
        self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
        for index in range(0, len(selectedArray_return)):
            isSelected: bool = selectedArray_return[index]
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(SELECTED_ARRAY_RETURN)
            stringBuffer.appendint(index)
            stringBuffer.append(SELECTED_SEP)
            stringBuffer.appendboolean(isSelected)
            self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
            if isSelected:
                selectedChoiceLabel: str = choiceGroup.getString(index)
                self.updateExclusive(selectedChoiceLabel)
    

    def isExclusive(self, itemLabel: str) -> bool:
        from org.allbinary.game.configuration.feature.GameFeatureChoiceGroups import GameFeatureChoiceGroups
        enumeration: Enumeration = GameFeatureChoiceGroups.getExclusiveInstance().get().keys()
        name: str = None
        while self.enumerationUtil.hasMoreElements(enumeration):
            name = self.enumerationUtil.nextElement(enumeration)
            if ((itemLabel > name) - (itemLabel < name)) == 0:
                return True
        return False
    

    # throws Exception
    def updateExclusive(self, selectedChoiceLabel: str) -> None:
        from org.allbinary.game.configuration.feature.Feature import Feature
        from org.allbinary.game.configuration.feature.GameFeatureChoiceGroups import GameFeatureChoiceGroups
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().ITEM_LABEL).append(selectedChoiceLabel)), self, "updateExclusive")
        gameFeature: Feature = Feature.getInstance(selectedChoiceLabel)
        hashtable: ABHashtable[object, object] = GameFeatureChoiceGroups.getExclusiveInstance().get()
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        basicArrayList: BasicArrayList = None
        anyType: object = None
        size: int = len(objectArray)
        for index in range(0, size):
            anyType = objectArray[index]
            basicArrayList = hashtable.get(anyType)
            self.updateExclusiveList(gameFeature, basicArrayList)
    

    # throws Exception
    def updateExclusiveList(self, gameFeature: Feature, list_: BasicArrayList) -> None:
        from org.allbinary.game.configuration.feature.Features import Features
        if list_.contains(gameFeature):
            features: Features = Features.getInstance()
            addIndex: int = list_.indexOf(gameFeature)
            size: int = list_.size()
            for index in range(0, size):
                if addIndex != index:
                    features.remove(list_.objectArray[index])
                else:
                    features.add(list_.objectArray[index])
# from java.util.Enumeration import Enumeration
# from javax.microedition.lcdui.ChoiceGroup import ChoiceGroup
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.EnumerationUtil import EnumerationUtil
from org.allbinary.util.HashtableUtil import HashtableUtil


GameFeatureUtil.instance = GameFeatureUtil()

