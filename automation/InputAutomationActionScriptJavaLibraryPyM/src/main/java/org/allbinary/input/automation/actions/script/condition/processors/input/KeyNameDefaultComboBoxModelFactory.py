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



class KeyNameDefaultComboBoxModelFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> DefaultComboBoxModel:
        from org.allbinary.input.automation.actions.script.condition.processors.input.DefaultComboBoxModel import DefaultComboBoxModel
        defaultComboBoxModel: DefaultComboBoxModel = DefaultComboBoxModel()
        keyArray: list[int] = KeySingletonFactory.getArray()
        for index in range(0, len(keyArray)):
            keyAsString: str = KeyEvent.getKeyText(keyArray[index])
            defaultComboBoxModel.addElement(keyAsString)
        return defaultComboBoxModel
# from java.awt.event.KeyEvent import KeyEvent
# from javax.swing import *
from org.allbinary.input.KeySingletonFactory import KeySingletonFactory


