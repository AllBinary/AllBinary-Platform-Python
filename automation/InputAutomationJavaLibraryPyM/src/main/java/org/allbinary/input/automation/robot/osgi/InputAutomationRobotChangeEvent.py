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
# package org.allbinary.input.automation.robot.osgi

from __future__ import annotations



class InputAutomationRobotChangeEvent:

    def _init_fields(self) -> None:
        self.inputAutomationRobotInterfaceWrapper: InputAutomationRobotInterfaceWrapper = None
    

    def __init__(self, inputAutomationRobotInterfaceWrapper: InputAutomationRobotInterfaceWrapper) -> None:
        self._init_fields()
        self.setInputAutomationRobotInterfaceWrapper(inputAutomationRobotInterfaceWrapper)
    

    def getInputAutomationRobotInterfaceWrapper(self) -> InputAutomationRobotInterfaceWrapper:
        return self.inputAutomationRobotInterfaceWrapper
    

    def setInputAutomationRobotInterfaceWrapper(self, inputAutomationRobotInterfaceWrapper: InputAutomationRobotInterfaceWrapper) -> None:
        self.inputAutomationRobotInterfaceWrapper = inputAutomationRobotInterfaceWrapper


