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
# package org.allbinary.input.automation.configuration

from __future__ import annotations



class InputAutomationConfigurationUtil:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getChangeEvent(inputAutomationModuleInterface: InputAutomationModuleFactoryInterface) -> InputAutomationConfigurationModuleChangeEvent:
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
        inputAutomationModuleConfiguration: InputAutomationModuleConfiguration = InputAutomationModuleConfiguration(inputAutomationModuleInterface)
        inputAutomationConfigurationModuleChangeEvent: InputAutomationConfigurationModuleChangeEvent = InputAutomationConfigurationModuleChangeEvent(inputAutomationModuleConfiguration)
        return inputAutomationConfigurationModuleChangeEvent
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration


