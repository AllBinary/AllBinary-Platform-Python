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

from org.allbinary.logic.StdUtil import StdUtil


class GameConfigurationTextInput:
    hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    SIMULATOR_IP: GameConfigurationTextInput = None
    SIMULATOR_PORT: GameConfigurationTextInput = None

    def _init_fields(self) -> None:
        self.label: str = StringUtil.getInstance().EMPTY_STRING
        self.text: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, label: str, text: str) -> None:
        self._init_fields()
        self.setText(text)
        self.setLabel(label)
        GameConfigurationTextInput.hashtable.put(self.getLabel(), self)
    

    @staticmethod
    def update(textField: TextField) -> None:
        anyType: object = textField.getLabel()
        gameConfigurationTextInput: GameConfigurationTextInput = GameConfigurationTextInput.hashtable.get(anyType)
        gameConfigurationTextInput.setText(textField.getString())
    

    def setText(self, text: str) -> None:
        self.text = text
    

    def getText(self) -> str:
        return self.text
    

    def setLabel(self, label: str) -> None:
        self.label = label
    

    def getLabel(self) -> str:
        return self.label
    

    @staticmethod
    def getHashtable() -> ABHashtable[object, object]:
        return GameConfigurationTextInput.hashtable
# from javax.microedition.lcdui.TextField import TextField
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.ABHashtable import ABHashtable


GameConfigurationTextInput.SIMULATOR_IP = GameConfigurationTextInput("IP: ", "192.168.1.3")

GameConfigurationTextInput.SIMULATOR_PORT = GameConfigurationTextInput("Port: ", "8010")

