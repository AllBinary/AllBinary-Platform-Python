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
# package org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class CssStyleValidation(Validation, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.cssStyleElementVector: BasicArrayList = None

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
        self.cssStyleElementVector = BasicArrayListD()
    

    def _constructor1(self, document: Document) -> None:
        super().__init__()
        self._init_fields()
        self.cssStyleElementVector = StylesValidationFactory.getInstance().getInstance(document)
    

    def _constructor1(self, hashMap: dict) -> None:
        super().__init__()
        self._init_fields()
        self.cssStyleElementVector = StylesValidationFactory.getInstance(hashMap)
    

    def isValid(self) -> bool:
        try:
            isValid: bool = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            size: int = self.cssStyleElementVector.size()
            for i in range(0, size):
                styleValidationInterface: ValidationInterface = self.cssStyleElementVector.get(i)
                if not styleValidationInterface.isValid():
                    isValid = False
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("End: " + str(isValid), self, self.commonStrings.IS_VALID)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        node: Node = document.createElement(StylesData.getInstance().NAME)
        styleNode: Node = document.createElement(StyleData.getInstance().NAME)
        node.appendChild(styleNode)
        size: int = self.cssStyleElementVector.size()
        for i in range(0, size):
            styleDomNodeInterface: DomNodeInterface = self.cssStyleElementVector.get(i)
            styleNode.appendChild(styleDomNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.dhtml.style.StyleData import StyleData
from org.allbinary.logic.visual.dhtml.style.StylesData import StylesData
from org.allbinary.logic.visual.dhtml.style.StylesValidationFactory import StylesValidationFactory
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


