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
# package org.allbinary.input.automation.module.osgi

from __future__ import annotations

from org.osgi.framework.ServiceFactory import ServiceFactory


class InputAutomationModuleServiceFactory(ServiceFactory):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface] = None
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getService(self, bundle: Bundle, registration: ServiceRegistration) -> object:
        self.logUtil.putF(self.commonStrings.START, self, "getService")
        return InputAutomationModuleService(self.getInputAutomationModuleInterfaceArray())
    

    def ungetService(self, bundle: Bundle, registration: ServiceRegistration, service: object) -> None:
        pass
    

    def getInputAutomationModuleInterfaceArray(self) -> list[InputAutomationModuleFactoryInterface]:
        return self.inputAutomationModuleInterfaceArray
    

    def setInputAutomationModuleInterfaceArray(self, inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface]) -> None:
        self.inputAutomationModuleInterfaceArray = inputAutomationModuleInterfaceArray
from org.osgi.framework.Bundle import Bundle
from org.osgi.framework.ServiceRegistration import ServiceRegistration
from bundle.input.automation.module.InputAutomationModuleService import InputAutomationModuleService
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


