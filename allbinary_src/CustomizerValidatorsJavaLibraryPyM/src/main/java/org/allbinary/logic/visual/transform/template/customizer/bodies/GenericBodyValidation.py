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
# package org.allbinary.logic.visual.transform.template.customizer.bodies

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class GenericBodyValidation(*java_bases(Validation, DomNodeInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.body: str = None

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
        from org.allbinary.logic.string.StringUtil import StringUtil
        super().__init__()
        self._init_fields()
        self.body = StringUtil.getInstance().EMPTY_STRING
    

    def _constructor1_1(self, document: Document) -> None:
        from org.allbinary.data.tree.dom.DomData import DomData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        super().__init__()
        self._init_fields()
        nodeList: NodeList = document.getElementsByTagName(BodyData.getInstance().NAME)
        for index in range(0, nodeList.getLength()):
            aBodyNode: Node = nodeList.item(index)
            aBodyValueNode: Node = DomSearchHelper.getNode(DomData.VALUE, aBodyNode.getChildNodes())
            self.body = DomNodeHelper.getTextNodeValue(aBodyValueNode)
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        super().__init__()
        self._init_fields()
        self.getFormData(hashMap)
    

    # throws Exception
    def getFormData(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        self.body = hashMap.get(BodyData.getInstance().NAME)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            isValid: bool = True
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            if not StringValidationUtil.getInstance().isValidNotRequired(self.body, BodyData.getInstance().MIN, AbSqlData.MAXBLOB):
                isValid = False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("BodyValidation: " + str(isValid), self, self.commonStrings.IS_VALID)
            return isValid
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            if True:
                stringBuffer.append("Error: Data submitted is < ")
                stringBuffer.appendint(int(BodyData.getInstance().MIN))
                stringBuffer.append(" or > ")
                stringBuffer.appendint(int(AbSqlData.MAXBLOB))
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
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = ModDomHelper.createNameValueNodes(document, BodyData.getInstance().NAME, self.body)
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomData import DomData
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


