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
# package org.allbinary.business.user.commerce.money.payment.gateway

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class PaymentGatewayView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.paymentGatewayInterface: PaymentGatewayInterface = None
    

    def __init__(self, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        self._init_fields()
        self.paymentGatewayInterface = paymentGatewayInterface
    

    def getPaymentGatewayInterface(self) -> PaymentGatewayInterface:
        return self.paymentGatewayInterface
    

    # throws Exception
    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayMapping import PaymentGatewayMapping
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, "toXmlNode")
            hashMap: dict = PaymentGatewayMapping(self.paymentGatewayInterface).toHashMap()
            hashMap.putAll(self.toHashMap())
            paymentGatewayNode: Node = ModDomHelper.createNodeWithValueNodes(document, str(PaymentGatewayData.NAME), hashMap)
            return paymentGatewayNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlNode", e)
            raise e
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


