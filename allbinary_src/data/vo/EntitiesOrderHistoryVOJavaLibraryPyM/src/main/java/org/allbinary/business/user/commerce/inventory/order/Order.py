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

from java.lang.JavaRuntimeStatic import java_bases
# from java.io.Serializable import Serializable
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface


class Order(*java_bases(OrderInterface, object)):

    def _init_fields(self) -> None:
        if "basket" not in vars(self): self.basket: BasketInterface = None
        if "paymentMethod" not in vars(self): self.paymentMethod: str = None
        if "shippingType" not in vars(self): self.shippingType: str = None
        if "storeName" not in vars(self): self.storeName: str = None
        if "special" not in vars(self): self.special: str = None
        if "id" not in vars(self): self.id: str = None
        if "userComment" not in vars(self): self.userComment: str = None
        if "userCancelComment" not in vars(self): self.userCancelComment: str = None
        if "storeComment" not in vars(self): self.storeComment: str = None
        if "storeCancelComment" not in vars(self): self.storeCancelComment: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 6:
            __class__._constructor6(self, *args)
    

    def _constructor1(self, basket: BasketInterface) -> None:
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        from org.allbinary.logic.string.StringUtil import StringUtil
        __class__._init_fields(self)
        self.basket = basket
        self.id = None
        self.shippingType = StringUtil.getInstance().EMPTY_STRING
    

    def _constructor6(self, storeName: str, basket: BasketInterface, id: str, shippingType: str, special: str, paymentMethod: str) -> None:
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        __class__._init_fields(self)
        self.storeName = storeName
        self.basket = basket
        self.id = id
        self.shippingType = shippingType
        self.special = special
        self.paymentMethod = paymentMethod
    

    def isIdValid(self) -> bool:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if self.getId() is None or self.getId().compareTo(StringUtil.getInstance().EMPTY_STRING) == 0 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.getId()) > OrderHistoryData.MAXIDLEN or not (StringValidationUtil.getInstance().isNumber(self.getId())):
            return False
        return True
    

    def isValid(self) -> bool:
        return True
    

    def getIdValidationInfo(self) -> str:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        if self.getId() is None or self.getId().compareTo(EMPTY_STRING) == 0 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.getId()) > OrderHistoryData.MAXIDLEN or not (StringValidationUtil.getInstance().isNumber(self.getId())):
            return "Please enter a valid order Id < " + str(OrderHistoryData.MAXIDLEN) + " digits in length.<br>"
        return EMPTY_STRING
    

    def setShippingMethod(self, shippingType: str) -> None:
        self.shippingType = shippingType
    

    def setPaymentMethod(self, value: str) -> None:
        self.paymentMethod = value
    

    def setSpecial(self, special: str) -> None:
        self.special = special
    

    def setId(self, value: str) -> None:
        self.id = value
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
    

    def setUserComments(self, value: str) -> None:
        self.userComment = value
    

    def setUserCancelComments(self, value: str) -> None:
        self.userCancelComment = value
    

    def setStoreComments(self, value: str) -> None:
        self.storeComment = value
    

    def setStoreCancelComments(self, value: str) -> None:
        self.storeCancelComment = value
    

    def getBasket(self) -> BasketInterface:
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        return self.basket
    

    def getShippingMethod(self) -> str:
        return self.shippingType
    

    def getPaymentMethod(self) -> str:
        return self.paymentMethod
    

    def getSpecial(self) -> str:
        return self.special
    

    def getId(self) -> str:
        return self.id
    

    def getStoreName(self) -> str:
        return self.storeName
    

    def getUserComments(self) -> str:
        return self.userComment
    

    def getUserCancelComments(self) -> str:
        return self.userCancelComment
    

    def getStoreComments(self) -> str:
        return self.storeComment
    

    def getStoreCancelComments(self) -> str:
        return self.storeCancelComment
    

    def reviewOrder(self, paymentMethod: str) -> str:
        return "Create your own Order.reviewOrder"
    

    def viewOrder(self, paymentMethod: str) -> str:
        return "Create your own Order.viewOrder"
    

    def emailOrder(self, userName: str, paymentMethod: str, storeFrontInterface: StoreFrontInterface) -> str:
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        return "Create your own Order.emailOrder"
    

    def toHashMapOrder(self) -> HashMap:
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(PaymentData.METHOD, self.paymentMethod)
        hashMap.put(ShippingMethodData.NAME, self.shippingType)
        hashMap.put(StoreFrontData.getInstance().NAME, self.storeName)
        hashMap.put(EntryData.getInstance().SPECIAL, self.special)
        hashMap.put(OrderData.ID, self.id)
        hashMap.put(OrderData.CUSTOMERCOMMENT, self.userComment)
        hashMap.put(OrderData.CUSTOMERCANCELCOMMENT, self.userCancelComment)
        hashMap.put(OrderData.STORECOMMENT, self.storeComment)
        hashMap.put(OrderData.STORECANCELCOMMENT, self.storeCancelComment)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        hashMap: HashMap = self.toHashMapOrder()
        keySet: Set = hashMap.keySet()
        keyArray: list[object] = keySet.toArray()
        size: int = len(keyArray)
        node: Node = document.createElement(OrderData.ORDER)
        for i in range(0, size):
            name: str = keyArray[i]
            value: str = hashMap.get(name)
            value = StringUtil.getInstance().getNonNull(value)
            node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
        return node
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
# from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


