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
# package org.allbinary.logic.visual.transform.template.customizer.hedges.heading

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class HeadingValidation(Validation, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.title: TitleValidation = None
        self.logo: LogoValidation = None

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
        self.title = TitleValidation()
        self.logo = LogoValidation()
    

    def _constructor1(self, document: Document) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.hedges.heading.HeadingData import HeadingData
        super().__init__()
        self._init_fields()
        headingNodeList: NodeList = document.getElementsByTagName(HeadingData.NAME)
        titleNode: Node = DomSearchHelper.getNode(TitleData.getInstance().NAME, headingNodeList.item(0).getChildNodes())
        logoNode: Node = DomSearchHelper.getNode(LogoData.getInstance().NAME, headingNodeList.item(0).getChildNodes())
        self.title = TitleValidation(titleNode)
        self.logo = LogoValidation(logoNode)
    

    def _constructor1(self, hashMap: dict) -> None:
        super().__init__()
        self._init_fields()
        self.getFormData(hashMap)
    

    # throws Exception
    def getFormData(self, hashMap: dict) -> None:
        self.title = TitleValidation(hashMap)
        self.logo = LogoValidation(hashMap)
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            titleValid: bool = True
            logoValid: bool = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            if not self.title.isValid():
                titleValid = False
            if not self.logo.isValid():
                logoValid = False
            else:
                self.logo.processLogoFile()
            if not titleValid and not logoValid:
                valid = False
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("HeadingValidation: " + str(valid), self, self.commonStrings.IS_VALID)
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            valid: bool = True
            titleValid: bool = True
            logoValid: bool = True
            stringBuffer: StringMaker = StringMaker()
            if not self.title.isValid():
                titleValid = False
            if not self.logo.isValid():
                logoValid = False
            if not titleValid and not logoValid:
                valid = False
            if not valid:
                stringBuffer.append("Include a title and/or logo for the header.")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.transform.template.customizer.hedges.heading.HeadingData import HeadingData
        node: Node = document.createElement(HeadingData.NAME)
        node.appendChild(self.logo.toXmlNode(document))
        node.appendChild(self.title.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoValidation import LogoValidation
from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


