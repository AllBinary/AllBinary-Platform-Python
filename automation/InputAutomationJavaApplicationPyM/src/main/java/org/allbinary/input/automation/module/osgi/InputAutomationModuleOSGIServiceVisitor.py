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

from org.allbinary.osgi.OSGIServiceVisitorInterface import OSGIServiceVisitorInterface


class InputAutomationModuleOSGIServiceVisitor(OSGIServiceVisitorInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def visit(self, anyType: object) -> object:
        return self.visit(anyType)
    

    # Java overloaded method: Python keeps the last definition
    def visit(self, osgiServiceInterface: OSGIServiceInterface) -> bool:
        try:
            inputAutomationModuleService: InputAutomationModuleService = osgiServiceInterface
            inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface] = inputAutomationModuleService.getInputAutomationModuleInterfaceArray()
            for index in range(0, len(inputAutomationModuleInterfaceArray)):
                InputAutomationJFrame.getInstance().onAdd(InputAutomationConfigurationUtil.getChangeEvent(inputAutomationModuleInterfaceArray[index]))
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "visit", e)
            return False
from bundle.input.automation.module.InputAutomationModuleService import InputAutomationModuleService
from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
from org.allbinary.string.CommonStrings import CommonStrings


