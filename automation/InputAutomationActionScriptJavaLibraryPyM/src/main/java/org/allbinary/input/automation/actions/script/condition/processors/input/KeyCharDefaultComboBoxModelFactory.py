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
# package org.allbinary.input.automation.actions.script.condition.processors.input

from __future__ import annotations



class KeyCharDefaultComboBoxModelFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> DefaultComboBoxModel:
        from org.allbinary.input.automation.actions.script.condition.processors.input.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyStroke import KeyStroke
        defaultComboBoxModel: DefaultComboBoxModel = DefaultComboBoxModel()
        keyArray: list[int] = KeySingletonFactory.getArray()
        for index in range(0, len(keyArray)):
            nextKey: int = keyArray[index]
            keyStroke: KeyStroke = KeyStroke.getKeyStroke(int(nextKey), 0)
            keyChar: str = KeyStrokeMap.getChar(keyStroke)
            defaultComboBoxModel.addElement(str(keyChar))
        return defaultComboBoxModel
# from javax.swing import *
from abbot.tester.KeyStrokeMap import KeyStrokeMap
from org.allbinary.input.KeySingletonFactory import KeySingletonFactory


