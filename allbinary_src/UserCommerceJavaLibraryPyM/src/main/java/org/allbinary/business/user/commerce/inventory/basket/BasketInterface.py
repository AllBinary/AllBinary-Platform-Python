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
# package org.allbinary.business.user.commerce.inventory.basket

from __future__ import annotations



# Java interface
class BasketInterface:
    

    def addItem(self, id: str, num: str) -> None:
        raise NotImplementedError()
    

    def removeItem(self, id: str) -> None:
        raise NotImplementedError()
    

    def adjustItem(self, id: str, num: str) -> None:
        raise NotImplementedError()
    

    def getTotalWeight(self) -> str:
        raise NotImplementedError()
    

    def getNumberOfItems(self) -> int:
        raise NotImplementedError()
    

    def getIds(self) -> Set:
        raise NotImplementedError()
    

    def getItems(self) -> dict:
        raise NotImplementedError()
    

    def getNumberOf(self, product: str) -> int:
        raise NotImplementedError()
    

    # throws MoneyException
    def getSubTotal(self) -> Money:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.business.user.commerce.money.MoneyException import MoneyException


