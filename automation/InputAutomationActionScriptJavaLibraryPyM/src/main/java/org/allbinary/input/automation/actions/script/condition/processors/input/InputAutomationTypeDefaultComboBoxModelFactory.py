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



class InputAutomationTypeDefaultComboBoxModelFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance() -> DefaultComboBoxModel:
        from org.allbinary.input.automation.actions.script.condition.processors.input.DefaultComboBoxModel import DefaultComboBoxModel
        defaultComboBoxModel: DefaultComboBoxModel = DefaultComboBoxModel()
        set: Set = InputRobotFactory.getInstance().get().keySet()
        nameArray: list[object] = set.toArray()
        size: int = len(nameArray)
        for index in range(0, size):
            defaultComboBoxModel.addElement(nameArray[index])
        return defaultComboBoxModel
# from java.util.Set import Set
# from javax.swing import *
from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory


