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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.TagHelper import TagHelper


@java_inherited_overloads
class OrderHistoryHelper(TagHelper):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("weblisketSession", None)
        vars(self).setdefault("storeFrontInterface", None)
        vars(self).setdefault("propertiesHashMap", None)
        vars(self).setdefault("pageContext", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("streetAddress", None)
        vars(self).setdefault("id", None)
        vars(self).setdefault("groupId", None)
        vars(self).setdefault("status", None)
        vars(self).setdefault("newStatus", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "weblisketSession" not in vars(self): self.weblisketSession: WeblisketSession = None
        if "storeFrontInterface" not in vars(self): self.storeFrontInterface: StoreFrontInterface = None
        if "propertiesHashMap" not in vars(self): self.propertiesHashMap: HashMap = None
        if "pageContext" not in vars(self): self.pageContext: PageContext = None
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "streetAddress" not in vars(self): self.streetAddress: StreetAddress = None
        if "id" not in vars(self): self.id: str = None
        if "groupId" not in vars(self): self.groupId: str = None
        if "status" not in vars(self): self.status: str = None
        if "newStatus" not in vars(self): self.newStatus: str = None
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        super().__init__()
        __class__._init_fields(self)
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        storeName: str = propertiesHashMap.get(StoreFrontData.getInstance().NAME)
        self.newStatus = propertiesHashMap.get(OrderHistoryData.STATUS)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        self.id = self.request.getParameter(OrderData.ID)
        self.groupId = self.request.getParameter(ShippingMethodData.GROUP)
        if self.newStatus is None:
            self.newStatus = self.request.getParameter(OrderHistoryData.STATUS)
    

    def setOrderStatus(self) -> str:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryFactory import OrderHistoryFactory
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryInterface import OrderHistoryInterface
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityInterface import OrderHistoryEntityInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "setOrderStatus()")
            return "Error Setting Order Status"
        except Exception as e:
            error: str = "Failed to set order status"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus()", e)
            return error + "<br/>" + "Exception: " + str(e) + "<br/>"
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryFactory import OrderHistoryFactory
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryInterface import OrderHistoryInterface
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
# from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityInterface import OrderHistoryEntityInterface
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


