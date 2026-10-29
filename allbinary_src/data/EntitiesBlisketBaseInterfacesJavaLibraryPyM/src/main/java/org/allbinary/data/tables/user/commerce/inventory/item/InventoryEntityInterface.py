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
# package org.allbinary.data.tables.user.commerce.inventory.item

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class InventoryEntityInterface(BasicDataTableInterface):
    

    # throws MoneyException
    def getItem(self, id: str) -> ItemInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getItems(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        raise NotImplementedError()
    

    def getWeight(self, id: str) -> str:
        raise NotImplementedError()
    

    def deleteWhere(self, key: str, value: str) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        raise NotImplementedError()
    

    def update(self, updatedValues: dict) -> None:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.business.user.commerce.money.MoneyException import MoneyException


