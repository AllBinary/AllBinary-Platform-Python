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

from java.lang.JavaRuntimeStatic import lazy_static


class GameConfigurationTextInput:
    hashtable: ABHashtable[object, object] = None
    SIMULATOR_IP: GameConfigurationTextInput = None
    SIMULATOR_PORT: GameConfigurationTextInput = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.label: str = StringUtil.getInstance().EMPTY_STRING
        self.text: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, label: str, text: str) -> None:
        self._init_fields()
        self.setText(text)
        self.setLabel(label)
        GameConfigurationTextInput.hashtable.put(self.getLabel(), self)
    

    @staticmethod
    def update(textField: TextField) -> None:
        from javax.microedition.lcdui.TextField import TextField
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
        from org.allbinary.util.ABHashtable import ABHashtable
        return GameConfigurationTextInput.hashtable
# from javax.microedition.lcdui.TextField import TextField
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.util.ABHashtable import ABHashtable


def _GameConfigurationTextInput_hashtable() -> object:
    from org.allbinary.logic.StdUtil import StdUtil
    from org.allbinary.util.ABHashtable import ABHashtable
    return StdUtil.getInstance().createHashtable()

lazy_static(GameConfigurationTextInput, "hashtable", _GameConfigurationTextInput_hashtable)

def _GameConfigurationTextInput_SIMULATOR_IP() -> object:
    return GameConfigurationTextInput("IP: ", "192.168.1.3")

lazy_static(GameConfigurationTextInput, "SIMULATOR_IP", _GameConfigurationTextInput_SIMULATOR_IP)

def _GameConfigurationTextInput_SIMULATOR_PORT() -> object:
    return GameConfigurationTextInput("Port: ", "8010")

lazy_static(GameConfigurationTextInput, "SIMULATOR_PORT", _GameConfigurationTextInput_SIMULATOR_PORT)

