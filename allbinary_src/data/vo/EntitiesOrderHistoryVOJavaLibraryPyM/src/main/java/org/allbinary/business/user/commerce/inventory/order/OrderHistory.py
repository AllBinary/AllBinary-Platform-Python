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
# package org.allbinary.business.user.commerce.inventory.order

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import datetime
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.business.user.commerce.inventory.order.Order import Order
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryInterface import OrderHistoryInterface


@java_inherited_overloads
class OrderHistory(*java_bases(Order, OrderHistoryInterface)):
    def _java_defaults(self):
        vars(self).setdefault("userName", None)
        vars(self).setdefault("shippingAddress", None)
        vars(self).setdefault("billingAddress", None)
        vars(self).setdefault("payment", None)
        vars(self).setdefault("shipDate", None)
        vars(self).setdefault("orderDate", None)
        vars(self).setdefault("transDate", None)
        vars(self).setdefault("cancelDate", None)
        vars(self).setdefault("status", None)
        vars(self).setdefault("subTotal", None)
        vars(self).setdefault("shippingCost", None)
        vars(self).setdefault("taxes", None)
        vars(self).setdefault("total", None)

    def _init_fields(self) -> None:
        if "userName" not in vars(self): self.userName: str = None
        if "shippingAddress" not in vars(self): self.shippingAddress: StreetAddress = None
        if "billingAddress" not in vars(self): self.billingAddress: StreetAddress = None
        if "payment" not in vars(self): self.payment: Payment = None
        if "shipDate" not in vars(self): self.shipDate: str = None
        if "orderDate" not in vars(self): self.orderDate: str = None
        if "transDate" not in vars(self): self.transDate: str = None
        if "cancelDate" not in vars(self): self.cancelDate: str = None
        if "status" not in vars(self): self.status: str = None
        if "subTotal" not in vars(self): self.subTotal: Money = None
        if "shippingCost" not in vars(self): self.shippingCost: Money = None
        if "taxes" not in vars(self): self.taxes: Money = None
        if "total" not in vars(self): self.total: Money = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__.__jconstructor2(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "BasketInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "OrderHistory" for base in type(args[1]).__mro__)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)
    

    def _constructor1(self, basketInterface: BasketInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        super().__init__(basketInterface)
        __class__._init_fields(self)
    

    def _constructor2_1(self, basketInterface: BasketInterface, orderHistory: OrderHistory) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        super().__init__(orderHistory.getStoreName(), basketInterface, orderHistory.getId(), orderHistory.getShippingMethod(), orderHistory.getSpecial(), orderHistory.getPaymentMethod())
        __class__._init_fields(self)
        self.userName = orderHistory.getUserName()
        self.shippingAddress = orderHistory.getShippingAddress()
        self.billingAddress = orderHistory.getBillingAddress()
        self.payment = orderHistory.getPaymentInfo()
        self.shipDate = orderHistory.getShipDate()
        self.orderDate = orderHistory.getOrderDate()
        self.transDate = orderHistory.getTransDate()
        self.cancelDate = orderHistory.getCancelDate()
        self.status = orderHistory.getStatus()
        self.subTotal = orderHistory.getSubTotal()
        self.shippingCost = orderHistory.getShippingCost()
        self.taxes = orderHistory.getTaxes()
        self.total = orderHistory.getTotal()
        java_super_call(super(), "setUserComments", orderHistory.getUserComments())
        java_super_call(super(), "setUserCancelComments", orderHistory.getUserCancelComments())
        java_super_call(super(), "setStoreComments", orderHistory.getStoreComments())
        java_super_call(super(), "setStoreCancelComments", orderHistory.getStoreCancelComments())
    

    def _constructor2_2(self, basketInterface: BasketInterface, orderHistoryHashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
        from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        from org.allbinary.business.user.commerce.money.Money import Money
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.business.user.commerce.money.payment.Payment import Payment
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        super().__init__(orderHistoryHashMap.get(StoreFrontData.getInstance().NAME), basketInterface, orderHistoryHashMap.get(OrderData.ID), orderHistoryHashMap.get(ShippingMethodData.NAME), orderHistoryHashMap.get(EntryData.getInstance().SPECIAL), orderHistoryHashMap.get(PaymentData.METHOD))
        __class__._init_fields(self)
        self.shippingAddress = StreetAddress(orderHistoryHashMap.get(ShippingAddressData.NAME), orderHistoryHashMap.get(ShippingAddressData.STREET), orderHistoryHashMap.get(ShippingAddressData.CITY), orderHistoryHashMap.get(ShippingAddressData.STATE), orderHistoryHashMap.get(ShippingAddressData.CODE), orderHistoryHashMap.get(ShippingAddressData.COUNTRY))
        self.billingAddress = StreetAddress(orderHistoryHashMap.get(BillingAddressData.NAME), orderHistoryHashMap.get(BillingAddressData.STREET), orderHistoryHashMap.get(BillingAddressData.CITY), orderHistoryHashMap.get(BillingAddressData.STATE), orderHistoryHashMap.get(BillingAddressData.CODE), orderHistoryHashMap.get(BillingAddressData.COUNTRY))
        self.payment = Payment(orderHistoryHashMap)
        self.userName = orderHistoryHashMap.get(UserData.USERNAME)
        self.orderDate = orderHistoryHashMap.get(OrderHistoryData.ORDERDATE)
        self.shipDate = orderHistoryHashMap.get(OrderHistoryData.SHIPPEDDATE)
        self.transDate = orderHistoryHashMap.get(OrderHistoryData.TRANSDATE)
        self.cancelDate = orderHistoryHashMap.get(OrderHistoryData.CANCELDATE)
        self.status = orderHistoryHashMap.get(OrderHistoryData.STATUS)
        self.subTotal = Money(orderHistoryHashMap.get(OrderHistoryData.SUBTOTAL))
        self.total = Money(orderHistoryHashMap.get(OrderHistoryData.TOTAL))
        self.shippingCost = Money(orderHistoryHashMap.get(OrderHistoryData.SHIPPINGCOST))
        self.taxes = Money(orderHistoryHashMap.get(OrderHistoryData.TAX))
        java_super_call(super(), "setUserComments", orderHistoryHashMap.get(OrderData.CUSTOMERCOMMENT))
        java_super_call(super(), "setUserCancelComments", orderHistoryHashMap.get(OrderData.CUSTOMERCANCELCOMMENT))
        java_super_call(super(), "setStoreComments", orderHistoryHashMap.get(OrderData.STORECOMMENT))
        java_super_call(super(), "setStoreCancelComments", orderHistoryHashMap.get(OrderData.STORECANCELCOMMENT))
    

    def setUserName(self, value: str) -> None:
        self.userName = value
    

    def setDefaultShippingAddress(self, shippingAddress: StreetAddress) -> None:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        self.shippingAddress = shippingAddress
    

    def setBillingAddress(self, billingAddress: StreetAddress) -> None:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        self.billingAddress = billingAddress
    

    def setPaymentInfo(self, payment: Payment) -> None:
        from org.allbinary.business.user.commerce.money.payment.Payment import Payment
        self.payment = payment
    

    def setShipDate(self, value: str) -> None:
        self.shipDate = value
    

    def setOrderDate(self, value: str) -> None:
        self.orderDate = value
    

    def setTransDate(self, value: str) -> None:
        self.transDate = value
    

    def setCancelDate(self, value: str) -> None:
        self.cancelDate = value
    

    def setStatus(self, value: str) -> None:
        self.status = value
    

    def setSubTotal(self, value: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.subTotal = value
    

    def setShippingCost(self, value: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.shippingCost = value
    

    def setTaxes(self, value: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.taxes = value
    

    def setTotal(self, value: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.total = value
    

    def getUserName(self) -> str:
        return self.userName
    

    def getShippingAddress(self) -> StreetAddress:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        return self.shippingAddress
    

    def getBillingAddress(self) -> StreetAddress:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        return self.billingAddress
    

    def getPaymentInfo(self) -> Payment:
        from org.allbinary.business.user.commerce.money.payment.Payment import Payment
        return self.payment
    

    def getShipDate(self) -> str:
        return self.shipDate
    

    def getOrderDate(self) -> str:
        return self.orderDate
    

    def getTransDate(self) -> str:
        return self.transDate
    

    def getCancelDate(self) -> str:
        return self.cancelDate
    

    def getStatus(self) -> str:
        return self.status
    

    def getSubTotal(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.subTotal
    

    def getShippingCost(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.shippingCost
    

    def getTaxes(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.taxes
    

    def getTotal(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.total
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(UserData.USERNAME, self.userName)
        hashMap.put(OrderHistoryData.ORDERDATE, self.orderDate)
        hashMap.put(OrderHistoryData.SHIPPEDDATE, self.shipDate)
        hashMap.put(OrderHistoryData.TRANSDATE, self.transDate)
        hashMap.put(OrderHistoryData.CANCELDATE, self.cancelDate)
        hashMap.put(OrderHistoryData.ORDERDATEFORMATTED, str(datetime.datetime(int(int(self.orderDate)))))
        hashMap.put(OrderHistoryData.SHIPPEDDATEFORMATTED, str(datetime.datetime(int(int(self.shipDate)))))
        hashMap.put(OrderHistoryData.TRANSDATEFORMATTED, str(datetime.datetime(int(int(self.transDate)))))
        hashMap.put(OrderHistoryData.CANCELDATEFORMATTED, str(datetime.datetime(int(int(self.cancelDate)))))
        hashMap.put(OrderHistoryData.STATUS, self.status)
        hashMap.put(OrderHistoryData.SUBTOTAL, str(self.subTotal))
        hashMap.put(OrderHistoryData.TOTAL, str(self.total))
        hashMap.put(OrderHistoryData.SHIPPINGCOST, str(self.shippingCost))
        hashMap.put(OrderHistoryData.TAX, str(self.taxes))
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
        from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        hashMap: HashMap = self.toHashMap()
        keySet: Set = hashMap.keySet()
        keyArray: list[object] = keySet.toArray()
        size: int = len(keyArray)
        node: Node = document.createElement(OrderHistoryData.ORDERHISTORY)
        node.appendChild(java_super_call(super(), "toXmlNode", document))
        billingAddressNode: Node = document.createElement(BillingAddressData.BILLINGADDRESS)
        billingAddressNode.appendChild(self.billingAddress.toXmlNode(document))
        shippingAddressNode: Node = document.createElement(ShippingAddressData.SHIPPINGADDRESS)
        shippingAddressNode.appendChild(self.shippingAddress.toXmlNode(document))
        node.appendChild(billingAddressNode)
        node.appendChild(shippingAddressNode)
        node.appendChild(self.payment.toXmlNode(document))
        for i in range(0, size):
            name: str = keyArray[i]
            value: str = hashMap.get(name)
            value = StringUtil.getInstance().getNonNull(value)
            node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
        return node
    

    def getPaymentMethod(self) -> str:
        return java_super_call(super(), "getPaymentMethod")
# from java.util.Date import Date
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
# from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
# from org.allbinary.business.user.commerce.money.Money import Money
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.business.user.commerce.money.payment.Payment import Payment
# from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


