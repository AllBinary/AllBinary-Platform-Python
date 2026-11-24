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



class InputAutomationConfigurationModuleChangeEvent:

    def _init_fields(self) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        self.inputAutomationModuleConfiguration: InputAutomationModuleConfiguration = None
    

    def __init__(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        self._init_fields()
        self.setInputAutomationModuleConfiguration(inputAutomationModuleConfiguration)
    

    def getInputAutomationModuleConfiguration(self) -> InputAutomationModuleConfiguration:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        return self.inputAutomationModuleConfiguration
    

    def setInputAutomationModuleConfiguration(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        self.inputAutomationModuleConfiguration = inputAutomationModuleConfiguration
# from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration


