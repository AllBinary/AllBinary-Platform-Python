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
# package views.admin.payment.gateways

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class PaymentGatewaysView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.paymentGatewayVector: BasicArrayList = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface, gatewayVector: BasicArrayList) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.paymentGatewayVector = gatewayVector
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        try:
            storeName: str = self.getTransformInfoInterface().getStoreName()
            paymentGatewaysNode: Node = document.createElement(PaymentGatewaysData.NAME)
            size: int = self.paymentGatewayVector.size()
            for index in range(0, size):
                paymentType: BasicPaymentType = self.paymentGatewayVector.get(index)
                hashMap: dict = paymentType.toHashMap()
                hashMap.put(EntryData.getInstance().DEFAULT, PaymentTypeUtil.getInstance().getDefault(storeName).getBasicPaymentType().getName())
                paymentGatewayNode: Node = ModDomHelper.createNodeWithValueNodes(document, str(PaymentGatewayData.NAME), hashMap)
                paymentGatewaysNode.appendChild(paymentGatewayNode)
            return paymentGatewaysNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            error: str = "Failed to view payment gateways"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            return error
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewaysData import PaymentGatewaysData
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


