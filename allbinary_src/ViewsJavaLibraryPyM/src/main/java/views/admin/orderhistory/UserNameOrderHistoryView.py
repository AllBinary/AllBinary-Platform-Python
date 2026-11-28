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
# package views.admin.orderhistory

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


@java_inherited_overloads
class UserNameOrderHistoryView(*java_bases(HttpStoreComponentView, ValidationComponentInterface, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("userName", None)
        vars(self).setdefault("shipped", None)
        vars(self).setdefault("partiallyShipped", None)
        vars(self).setdefault("processing", None)
        vars(self).setdefault("preprocessing", None)
        vars(self).setdefault("cancelled", None)
        vars(self).setdefault("ON", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "userName" not in vars(self): self.userName: str = None
        if "shipped" not in vars(self): self.shipped: str = None
        if "partiallyShipped" not in vars(self): self.partiallyShipped: str = None
        if "processing" not in vars(self): self.processing: str = None
        if "preprocessing" not in vars(self): self.preprocessing: str = None
        if "cancelled" not in vars(self): self.cancelled: str = None
        self.ON: str = "on"
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        self.request = self.getPageContext().getRequest()
        self.userName = self.request.getParameter(UserData.USERNAME)
        self.preprocessing = self.request.getParameter(OrderHistoryData.PREPROCESSINGNAME)
        self.shipped = self.request.getParameter(OrderHistoryData.SHIPPEDNAME)
        self.partiallyShipped = self.request.getParameter(OrderHistoryData.PARTIALLYSHIPPEDNAME)
        self.processing = self.request.getParameter(OrderHistoryData.PROCESSINGNAME)
        self.cancelled = self.request.getParameter(OrderHistoryData.CANCELLEDNAME)
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.addDomNodeInterfaces()
            return java_super_call(super(), "view")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntity import OrderHistoryEntity
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            node: Node = document.createElement(OrderData.ORDERS)
            orderHistoryEntity: OrderHistoryEntity = OrderHistoryEntity()
            orderReviewVector: BasicArrayList = orderHistoryEntity.getOrders(self.userName)
            size: int = orderReviewVector.size()
            for index in range(0, size):
                orderHistory: OrderHistory = orderReviewVector.get(index)
                orderHistoryNode: Node = orderHistory.toXmlNode(document)
                orderNode: Node = document.createElement(orderHistory.getPaymentMethod())
                node.appendChild(orderHistory.toXmlNode(document))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Attempt to View a users order history", self, "view")
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PREPROCESSINGNAME, OrderHistoryData.PREPROCESSING))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PROCESSINGNAME, OrderHistoryData.PROCESSING))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.CANCELLEDNAME, OrderHistoryData.CANCELLED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PARTIALLYSHIPPEDNAME, OrderHistoryData.PARTIALLYSHIPPED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.SHIPPEDNAME, OrderHistoryData.SHIPPED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, GLOBALS2.VIEWNAME, GLOBALS2.VIEW))
            return node
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

    def isValid(self) -> bool:
        from org.allbinary.business.user.username.UserName import UserName
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Started", self, self.commonStrings.IS_VALID)
        if UserName.getInstance().isValid(self.userName) == True:
            return True
        return False
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    def validationInfo(self) -> str:
        from org.allbinary.business.user.username.UserName import UserName
        if self.userName is None:
            return "No User Name Specified<br />"
        if UserName.getInstance().isValid(self.userName) == False:
            return "Invalid User Name<br />"
        return "Unknown Error<br />"
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.business.user.username.UserName import UserName
# from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntity import OrderHistoryEntity
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


