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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class LogoValidation(*java_bases(Validation, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("logoFileItem", None)
        vars(self).setdefault("logoAbPath", None)
        vars(self).setdefault("logoFile", None)
        vars(self).setdefault("isFile", False)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "logoFileItem" not in vars(self): self.logoFileItem: FileItem = None
        if "logoAbPath" not in vars(self): self.logoAbPath: AbPath = None
        if "logoFile" not in vars(self): self.logoFile: str = None
        if "isFile" not in vars(self): self.isFile: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.isFile = False
        self.logoAbPath = None
        self.logoFile = None
    

    def _constructor1_1(self, node: Node) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Node import Node
        super().__init__()
        __class__._init_fields(self)
        self.isFile = False
        self.logoAbPath = AbPath(DomSearchHelper.getNode(LogoData.getInstance().IMAGEPATH, node.getChildNodes()).getNodeValue(), StringUtil.getInstance().EMPTY_STRING)
        self.logoFile = DomSearchHelper.getNode(LogoData.getInstance().IMAGEFILENAME, node.getChildNodes()).getNodeValue()
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        super().__init__()
        __class__._init_fields(self)
        self.isFile = True
        self.getFormData(hashMap)
    

    # throws Exception
    def getFormData(self, hashMap: HashMap) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self.logoFileItem = hashMap.get(LogoData.getInstance().IMAGE)
        self.logoAbPath = AbPath(hashMap.get(LogoData.getInstance().IMAGEPATH), StringUtil.getInstance().EMPTY_STRING)
        if self.logoFileItem is not None:
            self.logoFile = HttpRequestUtil.getInstance().generateFileName(self.logoFileItem.getName())
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("HashMap: ")
            stringBuffer.append(str(hashMap))
            stringBuffer.append("\nLogoFileName: ")
            stringBuffer.append(self.logoFile)
            self.logUtil.putF(str(stringBuffer), self, "getFormData()")
    

    def isValid(self) -> bool:
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            valid: bool = True
            fileData: FileData = FileData.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("LogoValidation", self, self.commonStrings.IS_VALID)
            if not (StringValidationUtil.getInstance().isValidRequired(str(self.logoAbPath), 0, 512)):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("logoPath is invalid: " + str(self.logoAbPath), self, self.commonStrings.IS_VALID)
                return False
            if not (StringValidationUtil.getInstance().isValidRequired(self.logoFile, fileData.MINLEN, fileData.MAXLEN)):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("logoFile is invalid: " + self.logoFile, self, self.commonStrings.IS_VALID)
                return False
            if self.isFile:
                if self.logoFileItem is None:
                    return False
                if self.logoFileItem.getSize() > fileData.MAXIMAGEFILESIZE or self.logoFileItem.getSize() < fileData.MINIMAGEFILESIZE:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                        self.logUtil.putF("Image File Is Not The Right Size. " + str(fileData.MINIMAGEFILESIZE) + "< > " + str(fileData.MAXIMAGEFILESIZE), self, self.commonStrings.IS_VALID)
                    return False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Logo Validation: " + str(valid), self, self.commonStrings.IS_VALID)
            return valid
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Logo is not valid.")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringUtil: StringUtil = StringUtil.getInstance()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
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
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        hashMap: HashMap = self.toHashMap()
        return ModDomHelper.createNameValueNodes(document, LogoData.getInstance().NAME, hashMap)
    

    # throws Exception
    def processLogoFile(self) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoImageFileUtil import LogoImageFileUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Processing logoFile: ")
            stringBuffer.append(str(self.logoAbPath))
            stringBuffer.append(self.logoFile)
            self.logUtil.putF(str(stringBuffer), self, "processLogoFile()")
        LogoImageFileUtil(self.logoAbPath, self.logoFile).saveFiles(self.logoFileItem)
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.FileData import FileData
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


