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

from java.lang.JavaRuntimeStatic import java_bases
# from java.io.Serializable import Serializable
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface


class Basket(*java_bases(BasketInterface, object)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        self.items: HashMap = StdUtil.getInstance().createHashMap()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def addItem(self, id: str, num: str) -> None:
        if self.items.containsKey(id):
            oldNumStr: str = str(self.items.get(id))
            oldNumInt: int = str(oldNumStr)
            numInt: int = str(num)
            newNumInt: int = int(int(oldNumInt) + int(numInt))
            self.items.put(id, str(newNumInt))
        else:
            self.items.put(id, num)
    

    def removeItem(self, id: str) -> None:
        self.items.remove(id)
    

    def adjustItem(self, id: str, num: str) -> None:
        if int(str(num)) > 0:
            self.items.put(id, num)
        else:
            self.items.remove(id)
    

    def getTotalWeight(self) -> str:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.business.user.commerce.money.Money import Money
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
        itemsAndNumberInBasket: HashMap = self.getItems()
        totalWeight: Money = Money()
        if itemsAndNumberInBasket.size() > 0:
            items: Set = itemsAndNumberInBasket.keySet()
            product: str = None
            weightFloat: float = None
            itemArray: list[object] = items.toArray()
            size: int = len(itemArray)
            for index in range(0, size):
                product = str(itemArray[index])
                weightFloat = float(InventoryEntity().getWeight(product))
                weightFloat = float(float(self.getNumberOf(product)) * float(weightFloat))
                totalWeight.add(str(weightFloat))
        return str(totalWeight)
    

    def getNumberOfItems(self) -> int:
        return int(self.items.size())
    

    def getIds(self) -> Set:
        from java.util.Set import Set
        set: Set = self.items.keySet()
        return set
    

    def getItems(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.items
    

    def getNumberOf(self, product: str) -> int:
        numStr: str = self.items.get(product)
        return str(numStr)
    

    # throws MoneyException
    def getSubTotal(self) -> Money:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
        from org.allbinary.business.user.commerce.money.Money import Money
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        itemsAndNumberInBasket: HashMap = self.getItems()
        subTotal: Money = Money()
        if itemsAndNumberInBasket.size() > 0:
            items: Set = itemsAndNumberInBasket.keySet()
            inventoryEntityFactory: InventoryEntityFactory = InventoryEntityFactory.getInstance()
            inventoryEntity: InventoryEntity = inventoryEntityFactory.getInventoryEntityInstance()
            itemArray: list[object] = items.toArray()
            size: int = len(itemArray)
            for index in range(0, size):
                product: str = str(itemArray[index])
                itemInterface: ItemInterface = inventoryEntity.getItem(product)
                productTotal: Money = itemInterface.getPrice()
                productTotal.multiply(int(self.getNumberOf(product)))
                subTotal.add(str(productTotal))
        return subTotal
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
# from org.allbinary.business.user.commerce.money.Money import Money
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.logic.StdUtil import StdUtil


