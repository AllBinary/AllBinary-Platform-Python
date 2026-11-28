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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

import datetime
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


class TransformInfo(TransformInfoInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.isChild_field: bool = False
        if "name" not in vars(self): self.name: str = None
        if "storeName" not in vars(self): self.storeName: str = None
        if "objectFileName" not in vars(self): self.objectFileName: str = None
        if "anyType" not in vars(self): self.anyType: object = None
        if "objectConfigFileName" not in vars(self): self.objectConfigFileName: str = None
        if "objectConfigInterface" not in vars(self): self.objectConfigInterface: TransformInfoObjectConfigInterface = None
        if "template" not in vars(self): self.template: str = None
        if "templateFileName" not in vars(self): self.templateFileName: str = None
        if "dataFileName" not in vars(self): self.dataFileName: str = None
        self.data: str = StringUtil.getInstance().EMPTY_STRING

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 5:
            __class__._constructor5(self, *args)
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
    

    def _constructor1(self, name: str) -> None:
        __class__._init_fields(self)
        self.setName(name)
    

    def _constructor5(self, name: str, objectFileName: str, objectConfigFileName: str, templateFileName: str, dataFileName: str) -> None:
        __class__._init_fields(self)
        self.setName(name)
        self.setObjectFile(objectFileName)
        self.setObjectConfigFile(objectConfigFileName)
        self.setTemplateFile(templateFileName)
        self.setDataFile(dataFileName)
    

    # throws Exception
    def override(self, hashMap: HashMap) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.OutputTypeData import OutputTypeData
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.data.TransformInfoDataData import TransformInfoDataData
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
        from org.allbinary.logic.visual.transform.info.template.TransformInfoTemplateData import TransformInfoTemplateData
        from org.allbinary.logic.visual.transform.info.viewObject.TransformInfoObjectData import TransformInfoObjectData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        aName: str = hashMap.get(transformInfoData.NAME)
        if not (stringValidationUtil.isEmpty(aName)):
            self.name = aName
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("TransformInfo properties overridden for: ")
            stringBuffer.append(self.getName())
            stringBuffer.append("\n properties: ")
            stringBuffer.append(str(hashMap))
            self.logUtil.putF(str(stringBuffer), self, "override(HashMap hashMap)")
        aStoreName: str = hashMap.get(StoreFrontData.getInstance().NAME)
        if not (stringValidationUtil.isEmpty(aStoreName)):
            self.storeName = aStoreName
        aObjectFileName: str = hashMap.get(transformInfoData.OBJECTFILENAME)
        if not (stringValidationUtil.isEmpty(aObjectFileName)):
            self.objectFileName = aObjectFileName
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(URLGLOBALS.getMainPath())
        stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(self.storeName)
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        fileAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        aObject: str = hashMap.get(transformInfoData.OBJECT)
        if not (stringValidationUtil.isEmpty(aObject)):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("TransformInfo override view Object for: " + self.getName(), self, "override(HashMap hashMap)")
            fileDataString: str = CryptFileReader(TransformInfoObjectData.getInstance().UNCRYPTED_EXTENSION, TransformInfoObjectData.getInstance().ENCRYPTED_EXTENSION).get(AbPath(str(fileAbPath), aObject))
            if fileDataString is not None:
                self.anyType = fileDataString
        if not (stringValidationUtil.isEmpty(hashMap.get(transformInfoData.OBJECTCONFIG))):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("TransformInfo override ObjectConfig for: " + self.getName(), self, "override(HashMap hashMap)")
            self.setObjectConfig(hashMap.get(transformInfoData.OBJECTCONFIG))
        objectConfigFileName: str = hashMap.get(transformInfoData.OBJECTCONFIGFILENAME)
        if not (stringValidationUtil.isEmpty(objectConfigFileName)):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("TransformInfo override ObjectConfig File for: " + self.getName(), self, "override(HashMap hashMap)")
            self.setObjectConfigFile(objectConfigFileName)
        type_: str = hashMap.get(OutputTypeData.getInstance().NAME)
        if not (stringValidationUtil.isEmpty(type_)):
            if self.getObjectConfigInterface() is None:
                self.setObjectConfigInterface(TransformInfoObjectConfig(self))
            self.getObjectConfigInterface().setOutputTypeName(type_)
        aTemplateFileName: str = hashMap.get(transformInfoData.TEMPLATEFILENAME)
        if not (stringValidationUtil.isEmpty(aTemplateFileName)):
            self.templateFileName = aTemplateFileName
        aTemplate: str = hashMap.get(transformInfoData.TEMPLATE)
        if not (stringValidationUtil.isEmpty(aTemplate)):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("TransformInfo override Template for: " + self.getName(), self, "override(HashMap hashMap)")
            fileDataString: str = CryptFileReader(TransformInfoTemplateData.getInstance().UNCRYPTED_EXTENSION, TransformInfoTemplateData.getInstance().ENCRYPTED_EXTENSION).get(AbPath(str(fileAbPath), aTemplate))
            if not (stringValidationUtil.isEmpty(fileDataString)):
                self.template = fileDataString
        aDataFileName: str = hashMap.get(transformInfoData.DATAFILENAME)
        if not (stringValidationUtil.isEmpty(aDataFileName)):
            self.dataFileName = aDataFileName
        aData: str = hashMap.get(transformInfoData.DATA)
        if not (stringValidationUtil.isEmpty(aData)):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("TransformInfo override Data for: " + self.getName(), self, "override(HashMap hashMap)")
            fileDataString: str = CryptFileReader(TransformInfoDataData.getInstance().UNCRYPTED_EXTENSION, TransformInfoDataData.getInstance().ENCRYPTED_EXTENSION).get(AbPath(str(fileAbPath), aData))
            if not (stringValidationUtil.isEmpty(fileDataString)):
                self.data = fileDataString
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer = StringMaker()
            stringBuffer.append("Name: ")
            stringBuffer.append(aName)
            stringBuffer.append("\nTemp Object File: ")
            stringBuffer.append(aObject)
            stringBuffer.append("\nTemp Object Config File: ")
            stringBuffer.append(str(self.getObjectConfigFilePath()))
            stringBuffer.append("\nTemp Template File: ")
            stringBuffer.append(aTemplate)
            stringBuffer.append("\nTemp Data File: ")
            stringBuffer.append(aData)
            stringBuffer.append("\nStore Name: ")
            stringBuffer.append(aStoreName)
            stringBuffer.append("\nObjectFile: ")
            stringBuffer.append(self.getObjectFile())
            stringBuffer.append("->TransformInfo")
            self.logUtil.putF(str(stringBuffer), self, "TransformInfoInterface(HashMap)")
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
            self.logUtil.putF(self.log(), self, "override")
    

    def log(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Name: ")
        stringBuffer.append(self.name)
        stringBuffer.append("\nObject File: ")
        stringBuffer.append(self.objectFileName)
        stringBuffer.append("\nObject Config File Path: ")
        stringBuffer.append(self.getObjectConfigFile())
        stringBuffer.append("\nTemplate File: ")
        stringBuffer.append(self.templateFileName)
        stringBuffer.append("\nData File: ")
        stringBuffer.append(self.dataFileName)
        stringBuffer.append("\nStore Name: ")
        stringBuffer.append(self.storeName)
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append(self.getObjectFile())
        stringBuffer.append("->TransformInfo")
        stringBuffer.append("TransformInfoInterface(HashMap)")
        return str(stringBuffer)
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
    

    def getStoreName(self) -> str:
        return self.storeName
    

    def setObject(self, anyType: object) -> None:
        self.anyType = anyType
    

    def setObjectFile(self, value: str) -> None:
        self.objectFileName = value
    

    def setTemplate(self, value: str) -> None:
        self.template = value
    

    def setTemplateFile(self, value: str) -> None:
        self.templateFileName = value
    

    # throws Exception
    def setObjectConfigFileName(self, value: str) -> None:
        self.objectConfigFileName = value
    

    # throws Exception
    def setObjectConfigFile(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactory import TransformInfoObjectConfigAndManipulatorFactory
        self.objectConfigFileName = value
        self.setObjectConfigInterface(TransformInfoObjectConfigAndManipulatorFactory.getInstance().getInstance(self.abeClientInformation, self, self.getObjectConfigFilePath()))
    

    # throws Exception
    def setObjectConfig(self, value: str) -> None:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactory import TransformInfoObjectConfigAndManipulatorFactory
        from org.w3c.dom.Document import Document
        document: Document = DomDocumentHelper.create(value)
        self.setObjectConfigInterface(TransformInfoObjectConfigAndManipulatorFactory.getInstance().getInstance(self.abeClientInformation, self, document))
    

    def setDataFile(self, value: str) -> None:
        self.dataFileName = value
    

    def setData(self, value: str) -> None:
        self.data = value
    

    def getName(self) -> str:
        return self.name
    

    def getObject(self) -> object:
        return self.anyType
    

    def getObjectFile(self) -> str:
        return self.objectFileName
    

    def getTemplate(self) -> str:
        return self.template
    

    def getTemplateFile(self) -> str:
        return self.templateFileName
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbFilePath import AbFilePath
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbFilePath(self.getTemplateFile())
    

    # throws Exception
    def getObjectConfigFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbFilePath import AbFilePath
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbFilePath(self.getObjectConfigFile())
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbFilePath import AbFilePath
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbFilePath(self.getDataFile())
    

    def getObjectConfigFile(self) -> str:
        return self.objectConfigFileName
    

    def getData(self) -> str:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.data.TransformInfoDataData import TransformInfoDataData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        dataFileString: str = self.getDataFile()
        if not (stringValidationUtil.isEmpty(dataFileString)):
            try:
                fileData: str = CryptFileReader(TransformInfoDataData.getInstance().UNCRYPTED_EXTENSION, TransformInfoDataData.getInstance().ENCRYPTED_EXTENSION).get(self.getDataFilePath())
                if not (stringValidationUtil.isEmpty(self.data)):
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                        self.logUtil.putF("Data File overriding existing data: " + str(self.getDataFilePath()), self, "getData()")
                self.data = fileData
            except Exception as e:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                    self.logUtil.put("Could Not Load Data from: " + str(self.getDataFile()), self, "getData()", e)
        try:
            if not (stringValidationUtil.isEmpty(self.data)):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                    self.logUtil.putF("Data: " + XmlDocumentHelper.toString(DomDocumentHelper.create(self.data)), self, "getData()")
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Name: ")
                    stringBuffer.append(self.name)
                    stringBuffer.append("\nEmpty Data For: ")
                    stringBuffer.append(dataFileString)
                    stringBuffer.append("\nPath: ")
                    stringBuffer.append(self.getDataFilePath().toFileSystemString())
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                        self.logUtil.putF(str(stringBuffer), self, "getData()")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Could Not Preview Data: " + self.data, self, "getData()", e)
        return self.data
    

    # throws Exception
    def getDataDocument(self) -> Document:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        localData: str = self.getData()
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if stringValidationUtil.isEmpty(localData):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.putF("No Data So Creating New Document", self, "getDataDocument()")
            return DomDocumentHelper.create()
        else:
            document: Document = DomDocumentHelper.create(localData)
            return document
    

    def getDataFile(self) -> str:
        return self.dataFileName
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.control.crypt.Encoder import Encoder
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(transformInfoData.NAME, self.name)
        hashMap.put(StoreFrontData.getInstance().NAME, self.storeName)
        hashMap.put(transformInfoData.OBJECTFILENAME, self.objectFileName)
        hashMap.put(transformInfoData.OBJECT, self.anyType)
        hashMap.put(transformInfoData.OBJECTCONFIGFILENAME, self.getObjectConfigFile())
        hashMap.put(transformInfoData.OBJECTCONFIG, Encoder.encode(list(str(self.getObjectConfigInterface()).encode())))
        hashMap.put(transformInfoData.TEMPLATEFILENAME, self.templateFileName)
        hashMap.put(transformInfoData.TEMPLATE, self.template)
        hashMap.put(transformInfoData.DATAFILENAME, self.dataFileName)
        hashMap.put(transformInfoData.DATA, Encoder.encode(list(self.data.encode())))
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        hashMap.put(EntryData.getInstance().LASTMODIFIED, time)
        return hashMap
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.control.crypt.Encoder import Encoder
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.name)
        vector.add(self.storeName)
        vector.add(self.objectFileName)
        vector.add(self.anyType)
        vector.add(self.getObjectConfigFile())
        vector.add(Encoder.encode(list(str(self.getObjectConfigInterface()).encode())))
        vector.add(self.templateFileName)
        vector.add(self.template)
        vector.add(self.dataFileName)
        vector.add(Encoder.encode(list(self.data.encode())))
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        vector.add(time)
        vector.add(time)
        return vector
    

    def getKey(self) -> object:
        return self.getName()
    

    def setChild(self) -> None:
        self.isChild_field = True
    

    def isChild(self) -> bool:
        return self.isChild_field
    

    def getObjectConfigInterface(self) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
        return self.objectConfigInterface
    

    def setObjectConfigInterface(self, objectConfigInterface: TransformInfoObjectConfigInterface) -> None:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
        self.objectConfigInterface = objectConfigInterface
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.Encoder import Encoder
# from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
# from org.allbinary.logic.io.OutputTypeData import OutputTypeData
# from org.allbinary.logic.io.path.AbFilePath import AbFilePath
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
# from org.allbinary.logic.visual.transform.info.data.TransformInfoDataData import TransformInfoDataData
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactory import TransformInfoObjectConfigAndManipulatorFactory
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
# from org.allbinary.logic.visual.transform.info.template.TransformInfoTemplateData import TransformInfoTemplateData
# from org.allbinary.logic.visual.transform.info.viewObject.TransformInfoObjectData import TransformInfoObjectData
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


