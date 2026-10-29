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

from org.allbinary.business.user.commerce.inventory.item.BasicItem import BasicItem
from org.allbinary.business.user.commerce.inventory.item.OrderItemInterface import OrderItemInterface


class Item(BasicItem, OrderItemInterface):

    def _init_fields(self) -> None:
        self.group: str = None
        self.tax: str = None
        self.shippingType: str = None
        self.shippingCost: str = None
        self.shippedDate: str = None
        self.shippingAddress: StreetAddress = None
        self.special: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, itemHashMap: dict) -> None:
        super().__init__(itemHashMap)
        self._init_fields()
        self.setData(itemHashMap)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
        EMPTY: str = StringUtil.getInstance().EMPTY_STRING
        self.group = EMPTY
        self.tax = EMPTY
        self.shippingType = EMPTY
        self.shippingCost = EMPTY
        self.shippingAddress = StreetAddress()
    

    def setData(self, itemHashMap: dict) -> None:
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
        return self.shippingAddress
    

    def getSpecial(self) -> str:
        return self.special
    

    def toHashMap(self) -> dict:
        hashMap: dict = super().toHashMap()
        hashMap.put(ShippingMethodData.GROUP, self.group)
        hashMap.put(OrderHistoryData.TAX, self.tax)
        hashMap.put(ShippingMethodData.NAME, self.shippingType)
        hashMap.put(ShippingMethodData.COST, self.shippingCost)
        hashMap.put(OrderHistoryData.SHIPPEDDATE, self.shippedDate)
        hashMap.put(EntryData.getInstance().SPECIAL, self.special)
        return hashMap
# from java.util.HashMap import HashMap
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
from org.allbinary.logic.string.StringUtil import StringUtil


