#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# II
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.logic.visual.transform.template.customizer.includes.meta

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class MetasValidation(*java_bases(Validation, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("storeFrontInterface", None)
        vars(self).setdefault("metaValidationVector", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "storeFrontInterface" not in vars(self): self.storeFrontInterface: StoreFrontInterface = None
        if "metaValidationVector" not in vars(self): self.metaValidationVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, storeName: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.template.customizer.includes.meta.MetaValidation import MetaValidation
        from org.allbinary.logic.visual.transform.template.customizer.includes.meta.MetaValidation import MetaValidation
        from org.allbinary.logic.visual.transform.template.customizer.includes.meta.MetaValidation import MetaValidation
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeValuesData import HtmlMetaAttributeValuesData
        super().__init__()
        __class__._init_fields(self)
        self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.metaValidationVector = BasicArrayListD()
        contentValue: str = self.storeFrontInterface.getName() + " E-Commerce Site"
        keywordsMetaValidation: MetaValidation = MetaValidation(HtmlMetaAttributeDataFactory.getInstance().NAME, "Keywords", HtmlMetaAttributeValuesData.getInstance().KEYWORDS, contentValue)
        abstractMetaValidation: MetaValidation = MetaValidation(HtmlMetaAttributeDataFactory.getInstance().NAME, "Abstract", HtmlMetaAttributeValuesData.getInstance().ABSTRACT, contentValue)
        descriptionMetaValidation: MetaValidation = MetaValidation(HtmlMetaAttributeDataFactory.getInstance().NAME, "Description", HtmlMetaAttributeValuesData.getInstance().DESCRIPTION, contentValue)
        self.metaValidationVector.add(keywordsMetaValidation)
        self.metaValidationVector.add(abstractMetaValidation)
        self.metaValidationVector.add(descriptionMetaValidation)
    

    def _constructor1_2(self, document: Document) -> None:
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
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetasData import HtmlMetasData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(HtmlMetasData.getInstance().NAME)
        metaArray: list[MetaValidation] = self.metaValidationVector.toArrayType([None] * (self.metaValidationVector.size()))
        size: int = len(metaArray)
        for i in range(0, size):
            metaValidation: MetaValidation = metaArray[i]
            node.appendChild(metaValidation.toXmlNode(document))
        return node
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
# from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeValuesData import HtmlMetaAttributeValuesData
# from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetasData import HtmlMetasData
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


