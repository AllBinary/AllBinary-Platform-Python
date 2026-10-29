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
# package taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class OrderHistoryHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.propertiesHashMap: dict = None
        self.pageContext: PageContext = None
        self.request: HttpServletRequest = None
        self.streetAddress: StreetAddress = None
        self.id: str = None
        self.groupId: str = None
        self.status: str = None
        self.newStatus: str = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        storeName: str = propertiesHashMap.get(StoreFrontData.getInstance().NAME)
        self.newStatus = propertiesHashMap.get(OrderHistoryData.STATUS)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.getFormData()
    

    def getFormData(self) -> None:
        self.id = self.request.getParameter(OrderData.ID)
        self.groupId = self.request.getParameter(ShippingMethodData.GROUP)
        if self.newStatus is None:
            self.newStatus = self.request.getParameter(OrderHistoryData.STATUS)
    

    def setOrderStatus(self) -> str:
        try:
            success: str = "Status successfully set to: " + self.status
            orderReviewInterface: OrderHistoryInterface = OrderHistoryFactory.getInstance(self.id)
            status: str = orderReviewInterface.getStatus()
            if ((status > OrderHistoryData.CANCELLED) - (status < OrderHistoryData.CANCELLED)) == 0:
                return "Order " + self.id + " Already Cancelled<br/>"
            elif ((status > OrderHistoryData.SHIPPED) - (status < OrderHistoryData.SHIPPED)) == 0:
                return "Order " + self.id + " Already Shipped. You can't cancel a shipped order.<br/>"
            elif ((status > OrderHistoryData.PREPROCESSING) - (status < OrderHistoryData.PREPROCESSING)) == 0:
                return "Order " + self.id + " has been cancelled.<br/>"
            elif ((status > OrderHistoryData.PARTIALLYSHIPPED) - (status < OrderHistoryData.PARTIALLYSHIPPED)) == 0:
                return "Order " + self.id + " Partially Shipped. You can cancel unshipped items, but not the whole order.<br/>"
            elif ((status > OrderHistoryData.PROCESSING) - (status < OrderHistoryData.PROCESSING)) == 0:
                orderHistoryEntityInterface: OrderHistoryEntityInterface = OrderHistoryEntityFactory.getInstance()
                orderHistoryEntityInterface.setStatus(self.id, self.newStatus)
                return "Order " + self.id + " has been cancelled.<br/>"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "setOrderStatus()")
            return "Error Setting Order Status"
        except Exception as e:
            error: str = "Failed to set order status"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus()", e)
            return error + "<br/>" + "Exception: " + str(e) + "<br/>"
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryFactory import OrderHistoryFactory
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryInterface import OrderHistoryInterface
from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityInterface import OrderHistoryEntityInterface
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil


