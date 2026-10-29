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
# package org.allbinary.game.configuration

from __future__ import annotations



class GameConfiguration:
    MIN_VALUE: int = int(-2147483648)

    def _init_fields(self) -> None:
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.defaultValue: int = SmallIntegerSingletonFactory.getInstance().getAt(0)
        self.value: int = GameConfiguration.MIN_VALUE
        self.minValue: int = self.defaultValue
        self.maxValue: int = self.defaultValue
        self.modifiable: bool = BooleanFactory.getInstance().TRUE
    

    def __init__(self, name: str, defaultValue: int, minValue: int, maxValue: int) -> None:
        from org.allbinary.game.configuration.GameConfigurationSingleton import GameConfigurationSingleton
        self._init_fields()
        self.setName(name)
        self.setDefaultValue(defaultValue)
        self.value = self.getDefaultValue()
        self.setMinValue(minValue)
        self.setMaxValue(maxValue)
        GameConfigurationSingleton.getInstance().getHashtable().put(self.getName(), self)
    

    # throws Exception
    def setValue(self, value: int) -> None:
        if self.value != value:
            oldValue: int = self.value
            self.value = value
            GameFeatureEventHandler.getInstance().fireEvent(GameFeatureEvent(self, str(StringMaker().append(self.name).append(" value: from: ").appendint(int(int(oldValue))).append(" to ").appendint(int(int(self.value))))))
    

    def getValue(self) -> int:
        return self.value
    

    def setMaxValue(self, maxValue: int) -> None:
        self.maxValue = maxValue
    

    def getMaxValue(self) -> int:
        return self.maxValue
    

    def setMinValue(self, minValue: int) -> None:
        self.minValue = minValue
    

    def getMinValue(self) -> int:
        return self.minValue
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name
    

    def setDefaultValue(self, defaultValue: int) -> None:
        self.defaultValue = defaultValue
    

    def getDefaultValue(self) -> int:
        return self.defaultValue
    

    # throws Exception
    def setDefault(self) -> None:
        self.setValue(self.getDefaultValue())
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Name: ")
        stringBuffer.append(self.name)
        stringBuffer.append(" Min: ")
        stringBuffer.appendint(int(int(self.getMinValue())))
        stringBuffer.append(" Max: ")
        stringBuffer.appendint(int(int(self.getMaxValue())))
        stringBuffer.append(" Value: ")
        stringBuffer.appendint(int(int(self.getValue())))
        stringBuffer.append(" Default: ")
        stringBuffer.appendint(int(int(self.getDefaultValue())))
        stringBuffer.append(" Modifiable: ")
        stringBuffer.appendboolean(self.isModifiable())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def setModifiable(self, modifiable: bool) -> None:
        self.modifiable = modifiable
    

    def isModifiable(self) -> bool:
        return self.modifiable
from org.allbinary.game.configuration.event.GameFeatureEvent import GameFeatureEvent
from org.allbinary.game.configuration.event.GameFeatureEventHandler import GameFeatureEventHandler
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


