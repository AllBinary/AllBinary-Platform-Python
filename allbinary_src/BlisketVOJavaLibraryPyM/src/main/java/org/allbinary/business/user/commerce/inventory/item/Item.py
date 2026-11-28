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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.business.user.commerce.inventory.item.BasicItem import BasicItem
from org.allbinary.business.user.commerce.inventory.item.OrderItemInterface import OrderItemInterface


@java_inherited_overloads
class Item(*java_bases(BasicItem, OrderItemInterface)):
    def _java_defaults(self):
        vars(self).setdefault("group", None)
        vars(self).setdefault("tax", None)
        vars(self).setdefault("shippingType", None)
        vars(self).setdefault("shippingCost", None)
        vars(self).setdefault("shippedDate", None)
        vars(self).setdefault("shippingAddress", None)
        vars(self).setdefault("special", None)

    def _init_fields(self) -> None:
        if "group" not in vars(self): self.group: str = None
        if "tax" not in vars(self): self.tax: str = None
        if "shippingType" not in vars(self): self.shippingType: str = None
        if "shippingCost" not in vars(self): self.shippingCost: str = None
        if "shippedDate" not in vars(self): self.shippedDate: str = None
        if "shippingAddress" not in vars(self): self.shippingAddress: StreetAddress = None
        if "special" not in vars(self): self.special: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)
    

    def _constructor1(self, itemHashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        super().__init__(itemHashMap)
        __class__._init_fields(self)
        self.setData(itemHashMap)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.logic.string.StringUtil import StringUtil
        super().__init__()
        __class__._init_fields(self)
        EMPTY: str = StringUtil.getInstance().EMPTY_STRING
        self.group = EMPTY
        self.tax = EMPTY
        self.shippingType = EMPTY
        self.shippingCost = EMPTY
        self.shippingAddress = StreetAddress()
    

    def setData(self, itemHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        self.group = itemHashMap.get(ShippingMethodData.GROUP)
        self.tax = itemHashMap.get(OrderHistoryData.TAX)
        self.shippingType = itemHashMap.get(ShippingMethodData.NAME)
        self.shippingCost = itemHashMap.get(ShippingMethodData.COST)
        self.shippedDate = itemHashMap.get(OrderHistoryData.SHIPPEDDATE)
        itemHashMap.put(StreetAddressData.NAME, itemHashMap.get(ShippingAddressData.NAME))
        itemHashMap.put(StreetAddressData.STREET, itemHashMap.get(ShippingAddressData.STREET))
        itemHashMap.put(StreetAddressData.CITY, itemHashMap.get(ShippingAddressData.CITY))
        itemHashMap.put(StreetAddressData.STATE, itemHashMap.get(ShippingAddressData.STATE))
        itemHashMap.put(StreetAddressData.CODE, itemHashMap.get(ShippingAddressData.CODE))
        itemHashMap.put(StreetAddressData.COUNTRY, itemHashMap.get(ShippingAddressData.COUNTRY))
        self.shippingAddress = StreetAddress(itemHashMap)
    

    def setGroup(self, value: str) -> None:
        self.group = value
    

    def setTax(self, value: str) -> None:
        self.tax = value
    

    def setShippingType(self, value: str) -> None:
        self.shippingType = value
    

    def setShippingCost(self, value: str) -> None:
        self.shippingCost = value
    

    def setShippingAddress(self, value: StreetAddress) -> None:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        self.shippingAddress = value
    

    def setSpecial(self, value: str) -> None:
        self.special = value
    

    def getGroup(self) -> str:
        return self.group
    

    def getTax(self) -> str:
        return self.tax
    

    def getShippingType(self) -> str:
        return self.shippingType
    

    def getShippingCost(self) -> str:
        return self.shippingCost
    

    def getShippingAddress(self) -> StreetAddress:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        return self.shippingAddress
    

    def getSpecial(self) -> str:
        return self.special
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        hashMap: HashMap = java_super_call(super(), "toHashMap")
        hashMap.put(ShippingMethodData.GROUP, self.group)
        hashMap.put(OrderHistoryData.TAX, self.tax)
        hashMap.put(ShippingMethodData.NAME, self.shippingType)
        hashMap.put(ShippingMethodData.COST, self.shippingCost)
        hashMap.put(OrderHistoryData.SHIPPEDDATE, self.shippedDate)
        hashMap.put(EntryData.getInstance().SPECIAL, self.special)
        return hashMap
# from java.util.HashMap import HashMap
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.logic.string.StringUtil import StringUtil


