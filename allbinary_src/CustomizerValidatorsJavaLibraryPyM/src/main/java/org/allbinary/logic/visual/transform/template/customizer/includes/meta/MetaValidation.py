#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# III
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.logic.visual.transform.template.customizer.includes.meta

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class MetaValidation(Validation, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.label: str = None
        self.name: str = None
        self.httpEquiv: str = None
        self.content: str = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            self._constructor4(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor4(self, htmlMetaAttributeData: HtmlMetaAttributeData, label: str, attributeValue: str, contentValue: str) -> None:
        super().__init__()
        self._init_fields()
        self.label = label
        if htmlMetaAttributeData.equals(HtmlMetaAttributeDataFactory.getInstance().HTTP_EQUIV):
            self.httpEquiv = attributeValue
        elif htmlMetaAttributeData.equals(HtmlMetaAttributeDataFactory.getInstance().NAME):
            self.name = attributeValue
        self.content = contentValue
    

    def _constructor1(self, document: Document) -> None:
        super().__init__()
        self._init_fields()
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
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
        hashMap: dict = StdUtil.getInstance().createHashMap()
        htmlMetaAttributeDataFactory: HtmlMetaAttributeDataFactory = HtmlMetaAttributeDataFactory.getInstance()
        hashMap.put(str(HtmlMetaData.getInstance().LABEL), self.label)
        hashMap.put(str(htmlMetaAttributeDataFactory.NAME), self.name)
        hashMap.put(str(htmlMetaAttributeDataFactory.HTTP_EQUIV), self.httpEquiv)
        hashMap.put(str(htmlMetaAttributeDataFactory.CONTENT), self.content)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        node: Node = ModDomHelper.createNameValueNodes(document, str(HtmlMetaData.getInstance().NAME), self.toHashMap())
        return node
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeData import HtmlMetaAttributeData
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaData import HtmlMetaData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


