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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_1(self, anyType: object) -> object:
        from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
        return self.visit(anyType)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_2(self, osgiServiceInterface: OSGIServiceInterface) -> bool:
        from bundle.input.automation.module.InputAutomationModuleService import InputAutomationModuleService
        from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
        try:
            inputAutomationModuleService: InputAutomationModuleService = osgiServiceInterface
            inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface] = inputAutomationModuleService.getInputAutomationModuleInterfaceArray()
            for index in range(0, len(inputAutomationModuleInterfaceArray)):
                InputAutomationJFrame.getInstance().onAdd(InputAutomationConfigurationUtil.getChangeEvent(inputAutomationModuleInterfaceArray[index]))
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "visit", e)
            return False

    def visit(self, *args):
        if len(args) == 1 and True:
            return self.visit_j1_1(*args)
        if len(args) == 1:
            return self.visit_j1_2(*args)
        return getattr(self, "visit_j" + str(len(args)))(*args)
# from bundle.input.automation.module.InputAutomationModuleService import InputAutomationModuleService
# from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
# from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
# from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
# from org.allbinary.string.CommonStrings import CommonStrings


