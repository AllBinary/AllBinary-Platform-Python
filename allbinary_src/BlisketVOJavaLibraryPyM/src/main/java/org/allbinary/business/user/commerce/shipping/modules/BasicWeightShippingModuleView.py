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
# package org.allbinary.business.user.commerce.shipping.modules

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.business.user.commerce.shipping.modules.BasicWeightShippingModule import BasicWeightShippingModule


class BasicWeightShippingModuleView(*java_bases(BasicWeightShippingModule, DomNodeInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def isValid(self) -> bool:
        return None
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    def validationInfo(self) -> str:
        return None
    

    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            shippingMethodNode: Node = document.createElement(ShippingMethodData.NAME)
            shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodData.NAME, self.getName()))
            shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodData.DESCRIPTION, self.getDescription()))
            return shippingMethodNode
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlNode", e)
            return None
    

    def toXmlDoc(self) -> Document:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            document: Document = DomDocumentHelper.create()
            return document
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlDoc", e)
            return None
    

    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return self.commonStrings.NOT_IMPLEMENTED
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view", e)
            return None
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


