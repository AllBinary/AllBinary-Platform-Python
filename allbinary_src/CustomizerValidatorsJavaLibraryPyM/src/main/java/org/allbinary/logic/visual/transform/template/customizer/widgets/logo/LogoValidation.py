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
# package org.allbinary.logic.visual.transform.template.customizer.widgets.logo

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class LogoValidation(Validation, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.logoFileItem: FileItem = None
        self.logoAbPath: AbPath = None
        self.logoFile: str = None
        self.isFile: bool = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
        self.isFile = False
        self.logoAbPath = None
        self.logoFile = None
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        super().__init__()
        self._init_fields()
        self.isFile = False
        self.logoAbPath = AbPath(DomSearchHelper.getNode(LogoData.getInstance().IMAGEPATH, node.getChildNodes()).getNodeValue(), StringUtil.getInstance().EMPTY_STRING)
        self.logoFile = DomSearchHelper.getNode(LogoData.getInstance().IMAGEFILENAME, node.getChildNodes()).getNodeValue()
    

    def _constructor1(self, hashMap: dict) -> None:
        super().__init__()
        self._init_fields()
        self.isFile = True
        self.getFormData(hashMap)
    

    # throws Exception
    def getFormData(self, hashMap: dict) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        self.logoFileItem = hashMap.get(LogoData.getInstance().IMAGE)
        self.logoAbPath = AbPath(hashMap.get(LogoData.getInstance().IMAGEPATH), StringUtil.getInstance().EMPTY_STRING)
        if self.logoFileItem is not None:
            self.logoFile = HttpRequestUtil.getInstance().generateFileName(self.logoFileItem.getName())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("HashMap: ")
            stringBuffer.append(str(hashMap))
            stringBuffer.append("\nLogoFileName: ")
            stringBuffer.append(self.logoFile)
            self.logUtil.putF(str(stringBuffer), self, "getFormData()")
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            fileData: FileData = FileData.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("LogoValidation", self, self.commonStrings.IS_VALID)
            if not StringValidationUtil.getInstance().isValidRequired(str(self.logoAbPath), 0, 512):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("logoPath is invalid: " + str(self.logoAbPath), self, self.commonStrings.IS_VALID)
                return False
            if not StringValidationUtil.getInstance().isValidRequired(self.logoFile, fileData.MINLEN, fileData.MAXLEN):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("logoFile is invalid: " + self.logoFile, self, self.commonStrings.IS_VALID)
                return False
            if self.isFile:
                if self.logoFileItem is None:
                    return False
                if self.logoFileItem.getSize() > fileData.MAXIMAGEFILESIZE or self.logoFileItem.getSize() < fileData.MINIMAGEFILESIZE:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                        self.logUtil.putF("Image File Is Not The Right Size. " + str(fileData.MINIMAGEFILESIZE) + "< > " + str(fileData.MAXIMAGEFILESIZE), self, self.commonStrings.IS_VALID)
                    return False
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Logo Validation: " + str(valid), self, self.commonStrings.IS_VALID)
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Logo is not valid.")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        stringUtil: StringUtil = StringUtil.getInstance()
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(LogoData.getInstance().IMAGE, stringUtil.EMPTY_STRING)
        if self.logoFile is not None:
            hashMap.put(LogoData.getInstance().IMAGEPATH, str(self.logoAbPath))
            hashMap.put(LogoData.getInstance().IMAGEFILENAME, self.logoFile)
        else:
            hashMap.put(LogoData.getInstance().IMAGEPATH, None)
            hashMap.put(LogoData.getInstance().IMAGEFILENAME, self.logoFile)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        hashMap: dict = self.toHashMap()
        return ModDomHelper.createNameValueNodes(document, LogoData.getInstance().NAME, hashMap)
    

    # throws Exception
    def processLogoFile(self) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoImageFileUtil import LogoImageFileUtil
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Processing logoFile: ")
            stringBuffer.append(str(self.logoAbPath))
            stringBuffer.append(self.logoFile)
            self.logUtil.putF(str(stringBuffer), self, "processLogoFile()")
        LogoImageFileUtil(self.logoAbPath, self.logoFile).saveFiles(self.logoFileItem)
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.FileData import FileData
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.apache.commons.fileupload.FileItem import FileItem
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


