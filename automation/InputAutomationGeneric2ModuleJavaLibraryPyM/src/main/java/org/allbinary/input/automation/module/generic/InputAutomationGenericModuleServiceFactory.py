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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.input.automation.module.osgi.InputAutomationModuleServiceFactory import InputAutomationModuleServiceFactory


@java_inherited_overloads
class InputAutomationGenericModuleServiceFactory(InputAutomationModuleServiceFactory):
    inputAutomationGenericModuleServiceFactory: InputAutomationGenericModuleServiceFactory = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.module.generic.GenericModuleFactory import GenericModuleFactory
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        super().__init__()
        __class__._init_fields(self)
        try:
            inputAutomationModuleInterfaceArray: list[InputAutomationModuleFactoryInterface] = [None] * (1)
            inputAutomationModuleInterfaceArray[0] = GenericModuleFactory()
            self.setInputAutomationModuleInterfaceArray(inputAutomationModuleInterfaceArray)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
    

    @staticmethod
    def getInstance() -> InputAutomationGenericModuleServiceFactory:
        return InputAutomationGenericModuleServiceFactory.inputAutomationGenericModuleServiceFactory
# from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _InputAutomationGenericModuleServiceFactory_inputAutomationGenericModuleServiceFactory() -> object:
    return InputAutomationGenericModuleServiceFactory()

lazy_static(InputAutomationGenericModuleServiceFactory, "inputAutomationGenericModuleServiceFactory", _InputAutomationGenericModuleServiceFactory_inputAutomationGenericModuleServiceFactory)

