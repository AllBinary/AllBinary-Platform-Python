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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class HeadingValidation(*java_bases(Validation, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("title", None)
        vars(self).setdefault("logo", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "title" not in vars(self): self.title: TitleValidation = None
        if "logo" not in vars(self): self.logo: LogoValidation = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoValidation import LogoValidation
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        super().__init__()
        __class__._init_fields(self)
        self.title = TitleValidation()
        self.logo = LogoValidation()
    

    def _constructor1_1(self, document: Document) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.template.customizer.hedges.heading.HeadingData import HeadingData
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoValidation import LogoValidation
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        super().__init__()
        __class__._init_fields(self)
        headingNodeList: NodeList = document.getElementsByTagName(HeadingData.NAME)
        titleNode: Node = DomSearchHelper.getNode(TitleData.getInstance().NAME, headingNodeList.item(0).getChildNodes())
        logoNode: Node = DomSearchHelper.getNode(LogoData.getInstance().NAME, headingNodeList.item(0).getChildNodes())
        self.title = TitleValidation(titleNode)
        self.logo = LogoValidation(logoNode)
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        super().__init__()
        __class__._init_fields(self)
        self.getFormData(hashMap)
    

    # throws Exception
    def getFormData(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoValidation import LogoValidation
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        self.title = TitleValidation(hashMap)
        self.logo = LogoValidation(hashMap)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            valid: bool = True
            titleValid: bool = True
            logoValid: bool = True
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            if not (java_predicate(self.title, "isValid")):
                titleValid = False
            if not (java_predicate(self.logo, "isValid")):
                logoValid = False
            else:
                self.logo.processLogoFile()
            if not (titleValid) and not (logoValid):
                valid = False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("HeadingValidation: " + str(valid), self, self.commonStrings.IS_VALID)
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
            valid: bool = True
            titleValid: bool = True
            logoValid: bool = True
            stringBuffer: StringMaker = StringMaker()
            if not (java_predicate(self.title, "isValid")):
                titleValid = False
            if not (java_predicate(self.logo, "isValid")):
                logoValid = False
            if not (titleValid) and not (logoValid):
                valid = False
            if not (valid):
                stringBuffer.append("Include a title and/or logo for the header.")
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
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.transform.template.customizer.hedges.heading.HeadingData import HeadingData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(HeadingData.NAME)
        node.appendChild(self.logo.toXmlNode(document))
        node.appendChild(self.title.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoData import LogoData
# from org.allbinary.logic.visual.transform.template.customizer.widgets.logo.LogoValidation import LogoValidation
# from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
# from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


