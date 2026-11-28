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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class CssStyleValidation(*java_bases(Validation, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("cssStyleElementVector", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "cssStyleElementVector" not in vars(self): self.cssStyleElementVector: BasicArrayList = None

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
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        super().__init__()
        __class__._init_fields(self)
        self.cssStyleElementVector = BasicArrayListD()
    

    def _constructor1_1(self, document: Document) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.dhtml.style.StylesValidationFactory import StylesValidationFactory
        from org.w3c.dom.Document import Document
        super().__init__()
        __class__._init_fields(self)
        self.cssStyleElementVector = StylesValidationFactory.getInstance().getInstance(document)
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.dhtml.style.StylesValidationFactory import StylesValidationFactory
        super().__init__()
        __class__._init_fields(self)
        self.cssStyleElementVector = StylesValidationFactory.getInstance(hashMap)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            isValid: bool = True
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            size: int = self.cssStyleElementVector.size()
            for i in range(0, size):
                styleValidationInterface: ValidationInterface = self.cssStyleElementVector.get(i)
                if not (java_predicate(styleValidationInterface, "isValid")):
                    isValid = False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("End: " + str(isValid), self, self.commonStrings.IS_VALID)
            return isValid
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
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
        from org.allbinary.logic.visual.dhtml.style.StyleData import StyleData
        from org.allbinary.logic.visual.dhtml.style.StylesData import StylesData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(StylesData.getInstance().NAME)
        styleNode: Node = document.createElement(StyleData.getInstance().NAME)
        node.appendChild(styleNode)
        size: int = self.cssStyleElementVector.size()
        for i in range(0, size):
            styleDomNodeInterface: DomNodeInterface = self.cssStyleElementVector.get(i)
            styleNode.appendChild(styleDomNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.dhtml.style.StyleData import StyleData
# from org.allbinary.logic.visual.dhtml.style.StylesData import StylesData
# from org.allbinary.logic.visual.dhtml.style.StylesValidationFactory import StylesValidationFactory
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


