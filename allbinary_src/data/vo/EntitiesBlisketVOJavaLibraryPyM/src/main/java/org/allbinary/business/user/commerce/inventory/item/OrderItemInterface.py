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

from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface


# Java interface
class OrderItemInterface(ItemInterface):
    

    def setGroup(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTax(self, value: str) -> None:
        raise NotImplementedError()
    

    def setShippingType(self, value: str) -> None:
        raise NotImplementedError()
    

    def setShippingCost(self, value: str) -> None:
        raise NotImplementedError()
    

    def setShippingAddress(self, value: StreetAddress) -> None:
        raise NotImplementedError()
    

    def setSpecial(self, value: str) -> None:
        raise NotImplementedError()
    

    def getGroup(self) -> str:
        raise NotImplementedError()
    

    def getTax(self) -> str:
        raise NotImplementedError()
    

    def getShippingType(self) -> str:
        raise NotImplementedError()
    

    def getShippingCost(self) -> str:
        raise NotImplementedError()
    

    def getShippingAddress(self) -> StreetAddress:
        raise NotImplementedError()
    

    def getSpecial(self) -> str:
        raise NotImplementedError()
from org.allbinary.business.user.address.StreetAddress import StreetAddress


