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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class OrderHistoryRequestHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.request: HttpServletRequest = None
        self.id: str = None
        self.groupId: str = None
        self.status: str = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        self.id = self.request.getParameter(OrderData.ID)
        self.groupId = self.request.getParameter(ShippingMethodData.GROUP)
        self.status = self.request.getParameter(OrderHistoryData.STATUS)
    

    def setOrderStatus(self) -> str:
        try:
            if ((self.groupId > CommonPhoneStrings.getInstance().ZERO) - (self.groupId < CommonPhoneStrings.getInstance().ZERO)) != 0:
                if OrderItemsEntityFactory.getInstance().isEverythingShipped(self.id):
                    self.status = OrderHistoryData.SHIPPED
                else:
                    self.status = OrderHistoryData.PARTIALLYSHIPPED
            success: str = "Status successfully set to: " + self.status
            OrderHistoryEntityFactory.getInstance().setStatus(self.id, self.status)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Success", self, "setOrderStatus()")
            return success
        except Exception as e:
            error: str = "Failed to set order status"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus()", e)
            return error
    

    # Java overloaded method: Python keeps the last definition
    def setOrderStatus(self, newStatus: str) -> str:
        try:
            if newStatus is None:
                newStatus = self.status
            success: str = "Status successfully set to: " + newStatus
            OrderHistoryEntityFactory.getInstance().setStatus(self.id, newStatus)
            orderHistory: OrderHistory = OrderHistoryEntityFactory.getInstance().getOrder(self.id)
            OrderStatusEmail(self.abeClientInformation, orderHistory).process()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Success", self, "setOrderStatus()")
            return success
        except Exception as e:
            error: str = "Failed to view order table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus(newStatus)", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.business.user.commerce.inventory.order.status.OrderStatusEmail import OrderStatusEmail
from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntityFactory import OrderItemsEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings


