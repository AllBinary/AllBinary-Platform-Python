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
# package org.allbinary.input.automation.module.generic

from __future__ import annotations

from org.allbinary.input.automation.module.osgi.InputAutomationModuleServiceFactory import InputAutomationModuleServiceFactory


class InputAutomationGenericModuleServiceFactory(InputAutomationModuleServiceFactory):
    inputAutomationGenericModuleServiceFactory: InputAutomationGenericModuleServiceFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        from org.allbinary.input.automation.module.generic.GenericModuleFactory import GenericModuleFactory
        super().__init__()
        self._init_fields()
        try:
            inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface] = [None] * (1)
            inputAutomationModuleInterfaceArray[0] = GenericModuleFactory()
            self.setInputAutomationModuleInterfaceArray(inputAutomationModuleInterfaceArray)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
    

    @staticmethod
    def getInstance() -> InputAutomationGenericModuleServiceFactory:
        return InputAutomationGenericModuleServiceFactory.inputAutomationGenericModuleServiceFactory
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil


InputAutomationGenericModuleServiceFactory.inputAutomationGenericModuleServiceFactory = InputAutomationGenericModuleServiceFactory()

