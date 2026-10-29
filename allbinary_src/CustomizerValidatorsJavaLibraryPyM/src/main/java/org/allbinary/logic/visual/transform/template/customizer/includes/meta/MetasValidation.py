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

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class MetasValidation(Validation, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.storeFrontInterface: StoreFrontInterface = None
        self.metaValidationVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, storeName: str) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.includes.meta.MetaValidation import MetaValidation
        from org.allbinary.logic.visual.transform.template.customizer.includes.meta.MetaValidation import MetaValidation
        from org.allbinary.logic.visual.transform.template.customizer.includes.meta.MetaValidation import MetaValidation
        super().__init__()
        self._init_fields()
        self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.metaValidationVector = BasicArrayListD()
        contentValue: str = self.storeFrontInterface.getName() + " E-Commerce Site"
        keywordsMetaValidation: MetaValidation = MetaValidation(HtmlMetaAttributeDataFactory.getInstance().NAME, "Keywords", HtmlMetaAttributeValuesData.getInstance().KEYWORDS, contentValue)
        abstractMetaValidation: MetaValidation = MetaValidation(HtmlMetaAttributeDataFactory.getInstance().NAME, "Abstract", HtmlMetaAttributeValuesData.getInstance().ABSTRACT, contentValue)
        descriptionMetaValidation: MetaValidation = MetaValidation(HtmlMetaAttributeDataFactory.getInstance().NAME, "Description", HtmlMetaAttributeValuesData.getInstance().DESCRIPTION, contentValue)
        self.metaValidationVector.add(keywordsMetaValidation)
        self.metaValidationVector.add(abstractMetaValidation)
        self.metaValidationVector.add(descriptionMetaValidation)
    

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
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        node: Node = document.createElement(HtmlMetasData.getInstance().NAME)
        metaArray: list[MetaValidation] = self.metaValidationVector.toArrayType([None] * (self.metaValidationVector.size()))
        size: int = len(metaArray)
        for i in range(0, size):
            metaValidation: MetaValidation = metaArray[i]
            node.appendChild(metaValidation.toXmlNode(document))
        return node
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeDataFactory import HtmlMetaAttributeDataFactory
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeValuesData import HtmlMetaAttributeValuesData
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetasData import HtmlMetasData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


