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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.TagHelper import TagHelper


@java_inherited_overloads
class UpdateOrderHelper(TagHelper):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("entryId", None)
        vars(self).setdefault("orderId", None)
        vars(self).setdefault("userName", None)
        vars(self).setdefault("storeName", None)
        vars(self).setdefault("shipDate", None)
        vars(self).setdefault("orderDate", None)
        vars(self).setdefault("transDate", None)
        vars(self).setdefault("cancelDate", None)
        vars(self).setdefault("status", None)
        vars(self).setdefault("paymentMethod", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("type_", None)
        vars(self).setdefault("expiration", None)
        vars(self).setdefault("number", None)
        vars(self).setdefault("encryption", None)
        vars(self).setdefault("billingName", None)
        vars(self).setdefault("billingStreet", None)
        vars(self).setdefault("billingCity", None)
        vars(self).setdefault("billingState", None)
        vars(self).setdefault("billingCode", None)
        vars(self).setdefault("billingCountry", None)
        vars(self).setdefault("shippingName", None)
        vars(self).setdefault("shippingStreet", None)
        vars(self).setdefault("shippingCity", None)
        vars(self).setdefault("shippingState", None)
        vars(self).setdefault("shippingCode", None)
        vars(self).setdefault("shippingCountry", None)
        vars(self).setdefault("shippingMethodName", None)
        vars(self).setdefault("subTotal", None)
        vars(self).setdefault("shippingCost", None)
        vars(self).setdefault("tax", None)
        vars(self).setdefault("total", None)
        vars(self).setdefault("special", None)
        vars(self).setdefault("userComment", None)
        vars(self).setdefault("userCancelComment", None)
        vars(self).setdefault("storeComment", None)
        vars(self).setdefault("storeCancelComment", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "entryId" not in vars(self): self.entryId: str = None
        if "orderId" not in vars(self): self.orderId: str = None
        if "userName" not in vars(self): self.userName: str = None
        if "storeName" not in vars(self): self.storeName: str = None
        if "shipDate" not in vars(self): self.shipDate: str = None
        if "orderDate" not in vars(self): self.orderDate: str = None
        if "transDate" not in vars(self): self.transDate: str = None
        if "cancelDate" not in vars(self): self.cancelDate: str = None
        if "status" not in vars(self): self.status: str = None
        if "paymentMethod" not in vars(self): self.paymentMethod: str = None
        if "name" not in vars(self): self.name: str = None
        if "type_" not in vars(self): self.type_: str = None
        if "expiration" not in vars(self): self.expiration: str = None
        if "number" not in vars(self): self.number: str = None
        if "encryption" not in vars(self): self.encryption: str = None
        if "billingName" not in vars(self): self.billingName: str = None
        if "billingStreet" not in vars(self): self.billingStreet: str = None
        if "billingCity" not in vars(self): self.billingCity: str = None
        if "billingState" not in vars(self): self.billingState: str = None
        if "billingCode" not in vars(self): self.billingCode: str = None
        if "billingCountry" not in vars(self): self.billingCountry: str = None
        if "shippingName" not in vars(self): self.shippingName: str = None
        if "shippingStreet" not in vars(self): self.shippingStreet: str = None
        if "shippingCity" not in vars(self): self.shippingCity: str = None
        if "shippingState" not in vars(self): self.shippingState: str = None
        if "shippingCode" not in vars(self): self.shippingCode: str = None
        if "shippingCountry" not in vars(self): self.shippingCountry: str = None
        if "shippingMethodName" not in vars(self): self.shippingMethodName: str = None
        if "subTotal" not in vars(self): self.subTotal: str = None
        if "shippingCost" not in vars(self): self.shippingCost: str = None
        if "tax" not in vars(self): self.tax: str = None
        if "total" not in vars(self): self.total: str = None
        if "special" not in vars(self): self.special: str = None
        if "userComment" not in vars(self): self.userComment: str = None
        if "userCancelComment" not in vars(self): self.userCancelComment: str = None
        if "storeComment" not in vars(self): self.storeComment: str = None
        if "storeCancelComment" not in vars(self): self.storeCancelComment: str = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        super().__init__()
        __class__._init_fields(self)
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
        from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        self.entryId = self.request.getParameter(EntryData.getInstance().ID)
        self.orderId = self.request.getParameter(OrderData.ID)
        self.userName = self.request.getParameter(UserData.USERNAME)
        self.storeName = self.request.getParameter(StoreFrontData.getInstance().NAME)
        self.shipDate = self.request.getParameter(OrderHistoryData.SHIPPEDDATE)
        self.orderDate = self.request.getParameter(OrderHistoryData.ORDERDATE)
        self.transDate = self.request.getParameter(OrderHistoryData.TRANSDATE)
        self.cancelDate = self.request.getParameter(OrderHistoryData.CANCELDATE)
        self.status = self.request.getParameter(OrderHistoryData.STATUS)
        self.paymentMethod = self.request.getParameter(PaymentData.METHOD)
        self.name = self.request.getParameter(PaymentData.NAME)
        self.type_ = self.request.getParameter(PaymentData.TYPE)
        self.expiration = self.request.getParameter(PaymentData.EXPIRATION)
        self.number = self.request.getParameter(PaymentData.NUMBER)
        self.encryption = self.request.getParameter(EntryData.getInstance().ENCRYPTION)
        self.billingName = self.request.getParameter(BillingAddressData.NAME)
        self.billingStreet = self.request.getParameter(BillingAddressData.STREET)
        self.billingCity = self.request.getParameter(BillingAddressData.CITY)
        self.billingState = self.request.getParameter(BillingAddressData.STATE)
        self.billingCode = self.request.getParameter(BillingAddressData.CODE)
        self.billingCountry = self.request.getParameter(BillingAddressData.COUNTRY)
        self.shippingName = self.request.getParameter(ShippingAddressData.NAME)
        self.shippingStreet = self.request.getParameter(ShippingAddressData.STREET)
        self.shippingCity = self.request.getParameter(ShippingAddressData.CITY)
        self.shippingState = self.request.getParameter(ShippingAddressData.STATE)
        self.shippingCode = self.request.getParameter(ShippingAddressData.CODE)
        self.shippingCountry = self.request.getParameter(ShippingAddressData.COUNTRY)
        self.shippingMethodName = self.request.getParameter(ShippingMethodData.NAME)
        self.subTotal = self.request.getParameter(OrderHistoryData.SUBTOTAL)
        self.shippingCost = self.request.getParameter(OrderHistoryData.SHIPPINGCOST)
        self.tax = self.request.getParameter(OrderHistoryData.TAX)
        self.total = self.request.getParameter(OrderHistoryData.TOTAL)
        self.special = self.request.getParameter(EntryData.getInstance().SPECIAL)
        self.userComment = self.request.getParameter(OrderData.CUSTOMERCOMMENT)
        self.userCancelComment = self.request.getParameter(OrderData.CUSTOMERCANCELCOMMENT)
        self.storeComment = self.request.getParameter(OrderData.STORECOMMENT)
        self.storeCancelComment = self.request.getParameter(OrderData.STORECANCELCOMMENT)
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
        from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successful update"
            orderHashMap: HashMap = StdUtil.getInstance().createHashMap()
            whereHashMap: HashMap = StdUtil.getInstance().createHashMap()
            orderHashMap.put(EntryData.getInstance().ID, self.entryId)
            orderHashMap.put(OrderData.ID, self.orderId)
            orderHashMap.put(UserData.USERNAME, self.userName)
            orderHashMap.put(StoreFrontData.getInstance().NAME, self.storeName)
            orderHashMap.put(OrderHistoryData.SHIPPEDDATE, self.shipDate)
            orderHashMap.put(OrderHistoryData.ORDERDATE, self.orderDate)
            orderHashMap.put(OrderHistoryData.TRANSDATE, self.transDate)
            orderHashMap.put(OrderHistoryData.CANCELDATE, self.cancelDate)
            orderHashMap.put(OrderHistoryData.STATUS, self.status)
            orderHashMap.put(PaymentData.METHOD, self.paymentMethod)
            orderHashMap.put(PaymentData.NAME, self.name)
            orderHashMap.put(PaymentData.TYPE, self.type_)
            orderHashMap.put(PaymentData.EXPIRATION, self.expiration)
            orderHashMap.put(BillingAddressData.NAME, self.billingName)
            orderHashMap.put(BillingAddressData.STREET, self.billingStreet)
            orderHashMap.put(BillingAddressData.CITY, self.billingCity)
            orderHashMap.put(BillingAddressData.STATE, self.billingState)
            orderHashMap.put(BillingAddressData.CODE, self.billingCode)
            orderHashMap.put(BillingAddressData.COUNTRY, self.billingCountry)
            orderHashMap.put(ShippingAddressData.NAME, self.shippingName)
            orderHashMap.put(ShippingAddressData.STREET, self.shippingStreet)
            orderHashMap.put(ShippingAddressData.CITY, self.shippingCity)
            orderHashMap.put(ShippingAddressData.STATE, self.shippingState)
            orderHashMap.put(ShippingAddressData.CODE, self.shippingCode)
            orderHashMap.put(ShippingAddressData.COUNTRY, self.shippingCountry)
            orderHashMap.put(ShippingMethodData.NAME, self.shippingMethodName)
            orderHashMap.put(OrderHistoryData.SUBTOTAL, self.subTotal)
            orderHashMap.put(OrderHistoryData.SHIPPINGCOST, self.shippingCost)
            orderHashMap.put(OrderHistoryData.TAX, self.tax)
            orderHashMap.put(OrderHistoryData.TOTAL, self.total)
            orderHashMap.put(EntryData.getInstance().SPECIAL, self.special)
            orderHashMap.put(OrderData.CUSTOMERCOMMENT, self.userComment)
            orderHashMap.put(OrderData.CUSTOMERCANCELCOMMENT, self.userCancelComment)
            orderHashMap.put(OrderData.STORECOMMENT, self.storeComment)
            orderHashMap.put(OrderData.STORECANCELCOMMENT, self.storeCancelComment)
            whereHashMap.put(OrderData.ID, self.orderId)
            OrderHistoryEntityFactory.getInstance().update(whereHashMap, orderHashMap)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update order table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
# from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
# from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


