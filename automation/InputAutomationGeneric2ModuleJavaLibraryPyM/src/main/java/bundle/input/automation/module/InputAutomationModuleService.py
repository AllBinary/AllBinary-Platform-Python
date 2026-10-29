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
# package bundle.input.automation.module

from __future__ import annotations

from bundle.input.automation.module.InputAutomationModuleServiceInterface import InputAutomationModuleServiceInterface


class InputAutomationModuleService(InputAutomationModuleServiceInterface):

    def _init_fields(self) -> None:
        self.inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface] = None
    

    def __init__(self, inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface]) -> None:
        self._init_fields()
        self.setInputAutomationModuleInterfaceArray(inputAutomationModuleInterfaceArray)
    

    def getInputAutomationModuleInterfaceArray(self) -> list[InputAutomationModuleFactoryInterface]:
        return self.inputAutomationModuleInterfaceArray
    

    def setInputAutomationModuleInterfaceArray(self, inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface]) -> None:
        self.inputAutomationModuleInterfaceArray = inputAutomationModuleInterfaceArray
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface


