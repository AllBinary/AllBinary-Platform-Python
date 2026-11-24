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


class OrderItemsRequestHelper(TagHelper):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.request: HttpServletRequest = None
        self.id: str = None
        self.groupId: str = None
        self.status: str = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        self.id = self.request.getParameter(OrderData.ID)
        self.groupId = self.request.getParameter(ShippingMethodData.GROUP)
        self.status = self.request.getParameter(OrderHistoryData.STATUS)
    

    def setOrderStatus_j1(self, newStatus: str) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntityFactory import OrderItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if newStatus is None:
                newStatus = self.status
            success: str = "Status successfully set to: " + newStatus
            OrderItemsEntityFactory.getInstance().setStatus(self.id, self.groupId, newStatus)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "setOrderStatus(newStatus)")
            return success
        except Exception as e:
            error: str = "Failed to view order table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus(newStatus)", e)
            return error
    

    def setOrderStatus_j0(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntityFactory import OrderItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Status successfully set to: " + self.status
            OrderItemsEntityFactory.getInstance().setStatus(self.id, self.groupId, self.status)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "setOrderStatus(newStatus)")
            return success
        except Exception as e:
            error: str = "Failed to view order table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus(newStatus)", e)
            return error

    def setOrderStatus(self, *args):
        return getattr(self, "setOrderStatus_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntityFactory import OrderItemsEntityFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


