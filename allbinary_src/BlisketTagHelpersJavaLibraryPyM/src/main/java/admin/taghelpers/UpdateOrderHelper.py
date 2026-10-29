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


class UpdateOrderHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.request: HttpServletRequest = None
        self.entryId: str = None
        self.orderId: str = None
        self.userName: str = None
        self.storeName: str = None
        self.shipDate: str = None
        self.orderDate: str = None
        self.transDate: str = None
        self.cancelDate: str = None
        self.status: str = None
        self.paymentMethod: str = None
        self.name: str = None
        self.type_: str = None
        self.expiration: str = None
        self.number: str = None
        self.encryption: str = None
        self.billingName: str = None
        self.billingStreet: str = None
        self.billingCity: str = None
        self.billingState: str = None
        self.billingCode: str = None
        self.billingCountry: str = None
        self.shippingName: str = None
        self.shippingStreet: str = None
        self.shippingCity: str = None
        self.shippingState: str = None
        self.shippingCode: str = None
        self.shippingCountry: str = None
        self.shippingMethodName: str = None
        self.subTotal: str = None
        self.shippingCost: str = None
        self.tax: str = None
        self.total: str = None
        self.special: str = None
        self.userComment: str = None
        self.userCancelComment: str = None
        self.storeComment: str = None
        self.storeCancelComment: str = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
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
        try:
            success: str = "Successful update"
            orderHashMap: dict = StdUtil.getInstance().createHashMap()
            whereHashMap: dict = StdUtil.getInstance().createHashMap()
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update order table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
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
from org.allbinary.logic.communication.log.LogUtil import LogUtil


