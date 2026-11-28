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

from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class MetaValidation(*java_bases(Validation, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("label", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("httpEquiv", None)
        vars(self).setdefault("content", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "label" not in vars(self): self.label: str = None
        if "name" not in vars(self): self.name: str = None
        if "httpEquiv" not in vars(self): self.httpEquiv: str = None
        if "content" not in vars(self): self.content: str = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            __class__._constructor4(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor4(self, htmlMetaAttributeData: HtmlMetaAttributeData, label: str, attributeValue: str, contentValue: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeData import HtmlMetaAttributeData
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
        super().__init__()
        __class__._init_fields(self)
        self.label = label
        if java_equals(htmlMetaAttributeData, HtmlMetaAttributeDataFactory.getInstance().HTTP_EQUIV):
            self.httpEquiv = attributeValue
        elif java_equals(htmlMetaAttributeData, HtmlMetaAttributeDataFactory.getInstance().NAME):
            self.name = attributeValue
        self.content = contentValue
    

    def _constructor1(self, document: Document) -> None:
        __class__._java_defaults(self)
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.w3c.dom.Document import Document
        super().__init__()
        __class__._init_fields(self)
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            valid: bool = True
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
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaData import HtmlMetaData
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        htmlMetaAttributeDataFactory: HtmlMetaAttributeDataFactory = HtmlMetaAttributeDataFactory.getInstance()
        hashMap.put(str(HtmlMetaData.getInstance().LABEL), self.label)
        hashMap.put(str(htmlMetaAttributeDataFactory.NAME), self.name)
        hashMap.put(str(htmlMetaAttributeDataFactory.HTTP_EQUIV), self.httpEquiv)
        hashMap.put(str(htmlMetaAttributeDataFactory.CONTENT), self.content)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaData import HtmlMetaData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = ModDomHelper.createNameValueNodes(document, str(HtmlMetaData.getInstance().NAME), self.toHashMap())
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeData import HtmlMetaAttributeData
# from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
# from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaData import HtmlMetaData
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


