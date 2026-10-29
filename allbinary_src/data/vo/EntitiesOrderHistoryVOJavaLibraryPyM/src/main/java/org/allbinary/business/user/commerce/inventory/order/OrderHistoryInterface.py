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



# Java interface
class OrderHistoryInterface:
    

    def setUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setDefaultShippingAddress(self, shippingAddress: StreetAddress) -> None:
        raise NotImplementedError()
    

    def setBillingAddress(self, billingAddress: StreetAddress) -> None:
        raise NotImplementedError()
    

    def setPaymentInfo(self, payment: Payment) -> None:
        raise NotImplementedError()
    

    def setShipDate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setOrderDate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTransDate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setCancelDate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setStatus(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSubTotal(self, value: Money) -> None:
        raise NotImplementedError()
    

    def setShippingCost(self, value: Money) -> None:
        raise NotImplementedError()
    

    def setTaxes(self, value: Money) -> None:
        raise NotImplementedError()
    

    def setTotal(self, value: Money) -> None:
        raise NotImplementedError()
    

    def getUserName(self) -> str:
        raise NotImplementedError()
    

    def getShippingAddress(self) -> StreetAddress:
        raise NotImplementedError()
    

    def getBillingAddress(self) -> StreetAddress:
        raise NotImplementedError()
    

    def getPaymentInfo(self) -> Payment:
        raise NotImplementedError()
    

    def getShipDate(self) -> str:
        raise NotImplementedError()
    

    def getOrderDate(self) -> str:
        raise NotImplementedError()
    

    def getTransDate(self) -> str:
        raise NotImplementedError()
    

    def getCancelDate(self) -> str:
        raise NotImplementedError()
    

    def getStatus(self) -> str:
        raise NotImplementedError()
    

    def getSubTotal(self) -> Money:
        raise NotImplementedError()
    

    def getShippingCost(self) -> Money:
        raise NotImplementedError()
    

    def getTaxes(self) -> Money:
        raise NotImplementedError()
    

    def getTotal(self) -> Money:
        raise NotImplementedError()
    

    def getPaymentMethod(self) -> str:
        raise NotImplementedError()
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.business.user.commerce.money.payment.Payment import Payment


