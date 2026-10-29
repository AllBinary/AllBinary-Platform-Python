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
# package views.generic.order

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class OrderView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.request: HttpServletRequest = None
        self.order: Order = None
        self.orderHistory: OrderHistory = None
        self.basketReview: BasketReview = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.request = self.getPageContext().getRequest()
        self.getFormData()
    

    # throws Exception
    def getFormData(self) -> None:
        id: str = self.request.getParameter(OrderData.ID)
        if id is None:
            id = self.getWeblisketSession().getOrder().getId()
        self.order = Order(Basket())
        self.order.setId(id)
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            orderHistoryNode: Node = self.orderHistory.toXmlNode(document)
            node: Node = document.createElement(self.orderHistory.getPaymentMethod())
            orderHistoryNode.appendChild(self.basketReview.toXmlNode(document))
            node.appendChild(orderHistoryNode)
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.commerce.inventory.basket.Basket import Basket
from org.allbinary.business.user.commerce.inventory.basket.BasketReview import BasketReview
from org.allbinary.business.user.commerce.inventory.order.Order import Order
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


