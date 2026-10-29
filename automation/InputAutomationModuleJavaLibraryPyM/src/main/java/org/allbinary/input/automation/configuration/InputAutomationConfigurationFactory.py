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



class InputAutomationConfigurationFactory:
    instance: InputAutomationConfigurationFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.inputAutomationConfiguration: InputAutomationConfiguration = None
    

    @staticmethod
    def getInstance() -> InputAutomationConfigurationFactory:
        return InputAutomationConfigurationFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface) -> None:
        from org.allbinary.input.automation.configuration.InputAutomationConfiguration import InputAutomationConfiguration
        from org.allbinary.input.automation.configuration.InputAutomationConfiguration import InputAutomationConfiguration
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        INPUT_AUTOMATION_CONFIGURATION: str = "InputAutomationConfiguration"
        file: File = InputAutomationConfiguration.getFile()
        if file.isFile():
            logUtil.putF("LoadingConfiguration", INPUT_AUTOMATION_CONFIGURATION, commonStrings.INIT)
            jaxbContext: JAXBContext = JAXBContext.newInstance(InputAutomationConfiguration)
            unmarshaller: Unmarshaller = jaxbContext.createUnmarshaller()
            root: JAXBElement[InputAutomationConfiguration] = unmarshaller.unmarshal(StreamSource(FileInputStream(file)), InputAutomationConfiguration)
            self.inputAutomationConfiguration = root.getValue()
            inputAutomationModuleConfigurationList: List[InputAutomationModuleConfiguration] = self.inputAutomationConfiguration.getInputAutomationModuleConfigurationList()
            logUtil.putF("isInstalled: " + str(self.inputAutomationConfiguration.isInstalled()) + " inputAutomationModuleConfigurationList: " + str(inputAutomationModuleConfigurationList), INPUT_AUTOMATION_CONFIGURATION, commonStrings.INIT)
            if inputAutomationModuleConfigurationList is not None:
                size: int = inputAutomationModuleConfigurationList.size()
                inputAutomationModuleConfiguration: InputAutomationModuleConfiguration = None
                for index in range(0, size):
                    inputAutomationModuleConfiguration = inputAutomationModuleConfigurationList.get(index)
                    inputAutomationModuleConfiguration.init(abeClientInformation)
            logUtil.putF("LoadedConfiguration", INPUT_AUTOMATION_CONFIGURATION, commonStrings.INIT)
        else:
            logUtil.putF("New Configuration", INPUT_AUTOMATION_CONFIGURATION, commonStrings.INIT)
            self.inputAutomationConfiguration = InputAutomationConfiguration()
# from java.io.File import File
# from java.io.FileInputStream import FileInputStream
# from java.util.List import List
# from javax.xml.bind.JAXBContext import JAXBContext
# from javax.xml.bind.JAXBElement import JAXBElement
# from javax.xml.bind.Unmarshaller import Unmarshaller
# from javax.xml.transform.stream.StreamSource import StreamSource
from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


InputAutomationConfigurationFactory.instance = InputAutomationConfigurationFactory()

