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

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.business.user.commerce.shipping.modules.PickUpShippingModule import PickUpShippingModule


class PickUpShippingModuleView(PickUpShippingModule, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def isValid(self) -> bool:
        return None
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def toXmlDoc(self) -> Document:
        return None
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            shippingMethodNode: Node = document.createElement(ShippingMethodData.NAME)
            shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodData.NAME, self.getName()))
            shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodData.DESCRIPTION, self.getDescription()))
            return shippingMethodNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlNode", e)
            return None
    

    def validationInfo(self) -> str:
        return None
    

    def view(self) -> str:
        return None
from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.w3c.dom.Node import Node


