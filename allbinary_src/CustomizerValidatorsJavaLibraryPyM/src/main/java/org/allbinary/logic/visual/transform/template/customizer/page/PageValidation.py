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
# package org.allbinary.logic.visual.transform.template.customizer.page

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class PageValidation(*java_bases(Validation, DomNodeInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.title: TitleValidation = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)
    

    def _constructor0(self) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        super().__init__()
        self._init_fields()
        self.title = TitleValidation()
    

    def _constructor1_1(self, document: Document) -> None:
        from org.allbinary.business.page.PageData import PageData
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        super().__init__()
        self._init_fields()
        node: Node = DomSearchHelper.getNode(TitleData.getInstance().NAME, document.getElementsByTagName(PageData.getInstance().NAME))
        self.title = TitleValidation(node)
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        super().__init__()
        self._init_fields()
        self.getFormData(hashMap)
    

    def getFormData(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
        self.title = TitleValidation(hashMap)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            valid: bool = True
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("PageValidation", self, self.commonStrings.IS_VALID)
            if not self.title.isValid():
                valid = False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("PageValidation: " + str(valid), self, self.commonStrings.IS_VALID)
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
            if not self.title.isValid():
                stringBuffer.append(self.title.validationInfo())
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
        from org.allbinary.business.page.PageData import PageData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(PageData.getInstance().NAME)
        node.appendChild(self.title.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.business.page.PageData import PageData
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
# from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleValidation import TitleValidation
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


