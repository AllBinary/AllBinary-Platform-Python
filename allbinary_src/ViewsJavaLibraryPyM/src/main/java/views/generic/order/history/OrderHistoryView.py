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
# package views.generic.order.history

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class OrderHistoryView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.request: HttpServletRequest = None
        self.shipped: str = None
        self.partiallyShipped: str = None
        self.processing: str = None
        self.preprocessing: str = None
        self.cancelled: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.request = self.getPageContext().getRequest()
        self.preprocessing = self.request.getParameter(OrderHistoryData.PREPROCESSINGNAME)
        self.shipped = self.request.getParameter(OrderHistoryData.SHIPPEDNAME)
        self.partiallyShipped = self.request.getParameter(OrderHistoryData.PARTIALLYSHIPPEDNAME)
        self.processing = self.request.getParameter(OrderHistoryData.PROCESSINGNAME)
        self.cancelled = self.request.getParameter(OrderHistoryData.CANCELLEDNAME)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        try:
            node: Node = document.createElement(OrderData.ORDERS)
            orderHistoryEntity: OrderHistoryEntity = OrderHistoryEntity()
            orderReviewVector: BasicArrayList = orderHistoryEntity.getOrders(self.getWeblisketSession().getUserName())
            size: int = orderReviewVector.size()
            for index in range(0, size):
                orderHistory: OrderHistory = orderReviewVector.get(index)
                orderHistoryNode: Node = orderHistory.toXmlNode(document)
                orderNode: Node = document.createElement(orderHistory.getPaymentMethod())
                node.appendChild(orderHistory.toXmlNode(document))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Attempt to View a users order history", self, "view")
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PREPROCESSINGNAME, OrderHistoryData.PREPROCESSING))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PROCESSINGNAME, OrderHistoryData.PROCESSING))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.CANCELLEDNAME, OrderHistoryData.CANCELLED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PARTIALLYSHIPPEDNAME, OrderHistoryData.PARTIALLYSHIPPED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.SHIPPEDNAME, OrderHistoryData.SHIPPED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, self.GLOBALS2.VIEWNAME, self.GLOBALS2.VIEW))
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

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
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntity import OrderHistoryEntity
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


