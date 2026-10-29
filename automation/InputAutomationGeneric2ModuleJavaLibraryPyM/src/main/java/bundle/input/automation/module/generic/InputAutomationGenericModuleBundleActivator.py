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
# package bundle.input.automation.module.generic

from __future__ import annotations

from org.allbinary.input.automation.module.osgi.InputAutomationModuleBundleActivator import InputAutomationModuleBundleActivator


class InputAutomationGenericModuleBundleActivator(InputAutomationModuleBundleActivator):
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def init(self) -> None:
        inputAutomationGenericModuleServiceFactory: InputAutomationGenericModuleServiceFactory = InputAutomationGenericModuleServiceFactory.getInstance()
        self.setInputAutomationModuleInterface(inputAutomationGenericModuleServiceFactory.getInputAutomationModuleInterfaceArray())
        self.setServiceFactory(inputAutomationGenericModuleServiceFactory)
from org.allbinary.input.automation.module.generic.InputAutomationGenericModuleServiceFactory import InputAutomationGenericModuleServiceFactory


