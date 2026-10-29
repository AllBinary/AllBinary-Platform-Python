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



#name="inputAutomationConfiguration", 
class InputAutomationConfiguration:
    FILENAME: str = "InputAutomationConfig.xml"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.installed: bool = False
        self.inputAutomationModuleConfigurationList: List[InputAutomationModuleConfiguration] = None
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getFile() -> File:
        return File(InputAutomationConfiguration.FILENAME)
    

    def isInstalled(self) -> bool:
        return self.installed
    

    def setInstalled(self, installed: bool) -> None:
        self.installed = installed
        self.logUtil.putF("Installed: " + str(installed), self, "setIntalled")
    

    def getInputAutomationModuleConfigurationList(self) -> List[InputAutomationModuleConfiguration]:
        return self.inputAutomationModuleConfigurationList
    

    # throws Exception
    def save(self) -> None:
        document: Document = DomDocumentHelper.create()
        file: File = File(InputAutomationConfiguration.FILENAME)
        FileUtil.getInstance().copy(AbPath(file.getAbsolutePath(), StringUtil.getInstance().EMPTY_STRING), AbPath(str(file.getAbsolutePath()) + ".bak.xml", StringUtil.getInstance().EMPTY_STRING))
        jaxbContext: JAXBContext = JAXBContext.newInstance(InputAutomationConfiguration)
        marshaller: Marshaller = jaxbContext.createMarshaller()
        marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, True)
        marshaller.marshal(self, document)
        DomDocumentFileHelper.save(FileWrapperUtil.wrapFile(file), document)
# from java.io.File import File
# from java.util.List import List
# from javax.xml.bind.JAXBContext import JAXBContext
# from javax.xml.bind.Marshaller import Marshaller
# from javax.xml.bind.annotation.XmlAccessType import XmlAccessType
# from javax.xml.bind.annotation.XmlAccessorType import XmlAccessorType
# from javax.xml.bind.annotation.XmlElement import XmlElement
# from javax.xml.bind.annotation.XmlRootElement import XmlRootElement
# from javax.xml.bind.annotation.XmlType import XmlType
from org.allbinary.data.tree.dom.document.DomDocumentFileHelper import DomDocumentFileHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringUtil import StringUtil
from org.w3c.dom.Document import Document


