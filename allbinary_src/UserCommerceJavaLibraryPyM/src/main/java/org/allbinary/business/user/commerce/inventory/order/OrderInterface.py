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
class OrderInterface:
    

    def setShippingMethod(self, shippingType: str) -> None:
        raise NotImplementedError()
    

    def setPaymentMethod(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial(self, special: str) -> None:
        raise NotImplementedError()
    

    def setStoreName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setUserComments(self, value: str) -> None:
        raise NotImplementedError()
    

    def setUserCancelComments(self, value: str) -> None:
        raise NotImplementedError()
    

    def setStoreComments(self, value: str) -> None:
        raise NotImplementedError()
    

    def setStoreCancelComments(self, value: str) -> None:
        raise NotImplementedError()
    

    def getBasket(self) -> BasketInterface:
        raise NotImplementedError()
    

    def getShippingMethod(self) -> str:
        raise NotImplementedError()
    

    def getPaymentMethod(self) -> str:
        raise NotImplementedError()
    

    def getSpecial(self) -> str:
        raise NotImplementedError()
    

    def getId(self) -> str:
        raise NotImplementedError()
    

    def getStoreName(self) -> str:
        raise NotImplementedError()
    

    def getUserComments(self) -> str:
        raise NotImplementedError()
    

    def getUserCancelComments(self) -> str:
        raise NotImplementedError()
    

    def getStoreComments(self) -> str:
        raise NotImplementedError()
    

    def getStoreCancelComments(self) -> str:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface


